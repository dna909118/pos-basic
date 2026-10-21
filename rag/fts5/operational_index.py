#!/usr/bin/env python3
"""BYAR BARBER offline full-text retrieval; lexical search only, never authority."""
import argparse
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID_EXT = {'.md', '.json', '.py', '.yaml', '.yml', '.txt'}


def configuration():
    return json.loads((ROOT/'rag/fts5/config.json').read_text(encoding='utf-8'))


def is_excluded(rel, cfg):
    return any(rel == x or rel.startswith(x) for x in cfg['exclude_paths']) or rel in cfg['human_only']


def source_files(cfg):
    out = set()
    for source in cfg['index_sources']:
        if Path(source).is_absolute() or '..' in Path(source).parts:
            raise ValueError('Source must remain inside repository')
        p = ROOT / source
        if not p.exists():
            raise FileNotFoundError(f'Missing source: {source}')
        files = p.rglob('*') if p.is_dir() else [p]
        for f in files:
            if not f.is_file() or f.suffix.lower() not in VALID_EXT:
                continue
            rel = f.relative_to(ROOT).as_posix()
            if not is_excluded(rel, cfg) and not f.is_symlink():
                out.add(rel)
    return sorted(out)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def source_manifest(cfg):
    return [{'path': f, 'sha256': sha((ROOT/f).read_bytes())} for f in source_files(cfg)]


def git_commit():
    result = subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True)
    return result.stdout.strip() if result.returncode == 0 else None


def fingerprint(cfg, files):
    return sha(json.dumps({'config':cfg,'sources':files},sort_keys=True,ensure_ascii=False).encode())


def chunk(text, size, overlap):
    if size <= 0 or overlap < 0 or overlap >= size:
        raise ValueError('Invalid chunk sizing')
    start = 0
    while start < len(text):
        stop = min(start + size, len(text))
        if stop < len(text):
            boundary = text.rfind('\n', start + size//2, stop)
            if boundary > start:
                stop = boundary + 1
        yield text[start:stop]
        if stop == len(text):
            break
        start = max(start + 1, stop - overlap)


def db_path(cfg):
    p = (ROOT/cfg['local_path']).resolve()
    if not p.is_relative_to((ROOT/'rag/runtime').resolve()):
        raise ValueError('Runtime database must be inside rag/runtime/')
    return p


def build():
    cfg = configuration()
    files = source_manifest(cfg)
    snapshot = fingerprint(cfg,files)
    target = db_path(cfg)
    target.parent.mkdir(parents=True,exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=target.parent,prefix='.building-',suffix='.sqlite3')
    os.close(fd)
    count=0
    try:
        c=sqlite3.connect(tmp)
        try:
            c.executescript('''
                CREATE TABLE metadata (key TEXT PRIMARY KEY,value TEXT NOT NULL);
                CREATE TABLE documents(id INTEGER PRIMARY KEY,source_path TEXT NOT NULL,chunk_index INTEGER NOT NULL,content TEXT NOT NULL,source_sha256 TEXT NOT NULL,UNIQUE(source_path,chunk_index));
                CREATE VIRTUAL TABLE search_index USING fts5(content,content='documents',content_rowid='id',tokenize='unicode61 remove_diacritics 2');
                CREATE TRIGGER doc_insert AFTER INSERT ON documents BEGIN
                    INSERT INTO search_index(rowid,content) VALUES(new.id,new.content);
                END;
            ''')
            for f in files:
                rel=f['path']
                value=(ROOT/rel).read_text(encoding='utf-8',errors='replace')
                for i,s in enumerate(chunk(value,cfg['chunk_chars'],cfg['chunk_overlap'])):
                    c.execute('INSERT INTO documents(source_path,chunk_index,content,source_sha256) VALUES(?,?,?,?)',(rel,i,s,f['sha256']))
                    count+=1
            pairs={'fingerprint':snapshot,'source_count':str(len(files)),'chunk_count':str(count),'git_commit':git_commit() or 'not_a_git_checkout','engine':'sqlite-fts5','schema':'2'}
            c.executemany('INSERT INTO metadata(key,value) VALUES (?,?)',pairs.items())
            c.commit()
            if c.execute('PRAGMA quick_check').fetchone()[0]!='ok':
                raise RuntimeError('SQLite integrity check failed during build')
        finally:
            c.close()
        os.replace(tmp,target)
    finally:
        if os.path.exists(tmp):os.remove(tmp)
    return {'ready':True,'sources':len(files),'chunks':count,'database':cfg['local_path'],'git_commit':git_commit()}


def validate_db():
    cfg=configuration()
    target=db_path(cfg)
    if not target.is_file():return {'ready':False,'reason':'missing_index'}
    try:
        files=source_manifest(cfg)
        expected=fingerprint(cfg,files)
        c=sqlite3.connect(f'file:{target}?mode=ro',uri=True)
        try:
            if c.execute('PRAGMA quick_check').fetchone()[0]!='ok':
                return {'ready':False,'reason':'corrupt_index'}
            data=dict(c.execute('SELECT key,value FROM metadata').fetchall())
            if data.get('engine')!='sqlite-fts5' or data.get('schema')!='2':
                return {'ready':False,'reason':'invalid_schema'}
            if data.get('fingerprint')!=expected:
                return {'ready':False,'reason':'stale_sources'}
            rows=c.execute('SELECT count(*) FROM documents').fetchone()[0]
            if str(rows)!=data.get('chunk_count'):
                return {'ready':False,'reason':'invalid_chunk_count'}
            if c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='search_index'").fetchone()[0]!=1:
                return {'ready':False,'reason':'missing_search_index'}
            return {'ready':True,'sources':len(files),'chunks':rows,'git_commit':data.get('git_commit'),'database':cfg['local_path']}
        finally:c.close()
    except (sqlite3.DatabaseError,OSError,ValueError,FileNotFoundError,KeyError):
        return {'ready':False,'reason':'corrupt_or_unreadable_index'}


def search(q, top_k=5):
    st=validate_db()
    if not st['ready']:
        raise RuntimeError('Index unavailable: '+st['reason'])
    if not isinstance(q,str) or len(q.strip())==0 or len(q)>500 or not (1<=top_k<=100):
        raise ValueError('Invalid query or top_k')
    tokens=re.findall(r'[^\W_]+',q,flags=re.UNICODE)
    if not tokens:raise ValueError('Query contains no searchable tokens')
    # Force literal token OR search to prevent MATCH query grammar injection.
    expr=' OR '.join('"'+x.replace('"','')+'"' for x in tokens[:20])
    c=sqlite3.connect(f'file:{db_path(configuration())}?mode=ro',uri=True)
    try:
        rows=c.execute('''SELECT d.source_path,d.chunk_index,d.content,bm25(search_index)
          FROM search_index JOIN documents d ON search_index.rowid=d.id
          WHERE search_index MATCH ? ORDER BY bm25(search_index) ASC LIMIT ?''',(expr,top_k)).fetchall()
        return [{'source':p,'chunk':i,'text':text[:500],'rank':round(score,6)} for p,i,text,score in rows]
    finally:c.close()


def lookup(identifier, limit=8):
    # Deterministic ID reference lookup in canonical JSON; never use search rank for authorization.
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{1,79}',identifier):
        raise ValueError('Invalid canonical ID')
    sources=['rag/work_drafts.json','rag/requirements.json','rag/traceability.json','rag/storyboard_index.json','rag/screen_index.json']
    hits=[]
    def walk(node,path,trail):
        if len(hits)>=limit:return
        if isinstance(node,dict):
            if any(isinstance(v,str) and v==identifier for v in node.values()):
                hits.append({'source':path,'record':node})
                return
            for v in node.values():walk(v,path,trail+1)
        elif isinstance(node,list):
            for v in node:walk(v,path,trail+1)
    for f in sources:
        walk(json.loads((ROOT/f).read_text(encoding='utf-8')),f,0)
    return hits


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('build');sub.add_parser('status')
    q=sub.add_parser('query');q.add_argument('text');q.add_argument('--top-k',type=int,default=5)
    e=sub.add_parser('lookup');e.add_argument('identifier')
    args=ap.parse_args()
    try:
        if args.command=='build': r=build()
        elif args.command=='status':r=validate_db()
        elif args.command=='query':r={'results':search(args.text,args.top_k)}
        else:r={'results':lookup(args.identifier)}
        print(json.dumps(r,ensure_ascii=False,indent=2))
        if args.command=='status' and not r['ready']:return 1
    except (ValueError,RuntimeError,sqlite3.Error,FileNotFoundError) as ex:
        print(json.dumps({'error':str(ex)},ensure_ascii=False),file=sys.stderr);return 1
    return 0
if __name__=='__main__':sys.exit(main())
