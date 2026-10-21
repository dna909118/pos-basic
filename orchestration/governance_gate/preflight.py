#!/usr/bin/env python3
"""Fail-closed live GitHub approval validation for approved BYAR BARBER work.

The provider is authoritative for identity/current issue state; local canonical drafts
are authoritative for exact scope bytes. Tool only reads provider objects.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
REPO_RE=re.compile(r'^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$')
TOKEN_RE=re.compile(r'^BYAR-(APPROVE|REVOKE) ([A-Za-z0-9_-]+) revision=([A-Za-z0-9._-]+) sha256=([a-f0-9]{64})$')

class GateError(RuntimeError):pass

def load(relative):return json.loads((ROOT/relative).read_text(encoding='utf-8'))

def draft_file(local_id):
    if local_id.startswith('UMB-M'):
        p=ROOT/f'management/drafts/umbrellas/{local_id}.md'
    elif local_id.startswith('CI-'):
        matches=list((ROOT/'management/drafts/issues').glob(f'{local_id}_*.md'))+list((ROOT/'management/drafts/issues').glob(f'{local_id}.md'))
        if len(matches)!=1:raise GateError(f'{local_id}: missing/ambiguous canonical draft')
        p=matches[0]
    else:raise GateError('Only canonical Child/parent IDs supported')
    if not p.is_file():raise GateError('Canonical draft missing')
    return p

def canonical_scope_hash(local_id):return hashlib.sha256(draft_file(local_id).read_bytes()).hexdigest()

class GitHubRead:
    def __init__(self,repository,token):
        if not REPO_RE.fullmatch(repository):raise GateError('Invalid repository')
        if not token:raise GateError('GITHUB_TOKEN missing')
        self.repo=repository;self.token=token
    def get(self,path):
        req=urllib.request.Request('https://api.github.com/repos/'+self.repo+path,headers={'Authorization':'Bearer '+self.token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'byar-governance-gate'})
        try:
            with urllib.request.urlopen(req,timeout=15) as response:
                return json.load(response)
        except (urllib.error.HTTPError,urllib.error.URLError,TimeoutError,ValueError) as e:
            raise GateError('Provider read failed (never assume absence): '+str(e)) from e
    def issue(self,n):return self.get(f'/issues/{n}')
    def comments(self,n):
        all_comments=[]
        for page in range(1,11):
            page_comments=self.get(f'/issues/{n}/comments?per_page=100&page={page}')
            if not isinstance(page_comments,list):raise GateError('Invalid comment API response')
            all_comments.extend(page_comments)
            if len(page_comments)<100:return all_comments
        raise GateError('Approval comment pagination limit exceeded')


def approval(comments,local_id,revision,scope_hash,approvers):
    # Require most recent explicit approval/revoke for *this canonical ID* to match current scope.
    candidates=[]
    for c in comments:
        actor=c.get('user') or {}
        login=actor.get('login','')
        if login.casefold() not in approvers or actor.get('type')=='Bot':continue
        for line in c.get('body','').splitlines():
            match=TOKEN_RE.fullmatch(line.strip())
            if match and match.group(2)==local_id:
                candidates.append((c.get('created_at',''),c.get('id',0),match.group(1),match.group(3),match.group(4),login,c.get('html_url')))
    if not candidates:raise GateError(f'{local_id}: no authorized Human approval comment')
    last=max(candidates,key=lambda x:(x[0],x[1]))
    if last[2]!='APPROVE' or last[3]!=revision or last[4]!=scope_hash:
        raise GateError(f'{local_id}: approval revoked, stale, or wrong revision/hash')
    return {'approved_by':last[5],'evidence_url':last[6],'scope_revision':revision,'scope_sha256':scope_hash}


def verify_issue(issue,canonical_id,number,repo,milestone=None):
    if issue.get('number')!=number or issue.get('state')!='open' or 'pull_request' in issue:
        raise GateError(f'{canonical_id}: provider object is not an open Issue')
    if not issue.get('title','').startswith('['+canonical_id+']'):
        raise GateError(f'{canonical_id}: native Issue title does not bind canonical ID')
    if issue.get('repository_url','').rstrip('/')!='https://api.github.com/repos/'+repo:
        raise GateError(f'{canonical_id}: issue belongs to a different repository')
    if milestone is not None and (issue.get('milestone') or {}).get('number')!=milestone:
        raise GateError(f'{canonical_id}: wrong or absent Milestone binding')


def preflight(number,engine,repo,approvers,client):
    if engine not in {'opencode','mini-swe'}:raise GateError('Unrecognized engine')
    if not approvers:raise GateError('Explicit BYAR_HUMAN_APPROVERS allowlist required')
    registry=load('rag/provider_bindings.json')
    if registry.get('active_provider')!='github':raise GateError('GitHub not active')
    byid={x['local_id']:x for x in registry['bindings']}
    child=client.issue(number)
    m=re.match(r'^\[(CI-[A-Za-z0-9-]+)\]',child.get('title',''))
    if not m:raise GateError('Issue title lacks canonical Child ID')
    cid=m.group(1)
    if cid not in byid or byid[cid]['kind']!='child':raise GateError('Unknown canonical Child ID')
    binding=byid[cid]
    if binding['status']!='published' or binding['github']['number']!=number:
        raise GateError(f'{cid}: canonical provider binding not verified/published')
    if binding['github'].get('url')!=child.get('html_url'):
        raise GateError(f'{cid}: provider URL binding mismatch')
    mid=binding['milestone_id'];uid=binding['umbrella_id']
    mb=byid[mid];ub=byid[uid]
    if mb['status']!='published' or not isinstance(mb['github']['number'],int):
        raise GateError('Milestone not published')
    if ub['status']!='published' or not isinstance(ub['github']['number'],int):
        raise GateError('Umbrella not published')
    verify_issue(child,cid,number,repo,mb['github']['number'])
    parent=client.issue(ub['github']['number'])
    verify_issue(parent,uid,ub['github']['number'],repo,mb['github']['number'])
    if parent.get('html_url')!=ub['github'].get('url'):
        raise GateError('Umbrella bound URL mismatch')
    work=load('rag/work_drafts.json')
    current=next((x for x in work['child_issues'] if x['draft_id']==cid),None)
    umbrella=next((x for x in work['umbrellas'] if x['draft_id']==uid),None)
    if not current or not umbrella or cid not in umbrella['child_draft_ids']:
        raise GateError('Broken local canonical parent-child relationship')
    if current['milestone_id']!=mid or current['umbrella_id']!=uid:
        raise GateError('Broken local canonical milestone relationship')
    # Optional explicit canonical blockers: if present, require each closed with a verified binding.
    for dep in current.get('depends_on',[]):
        b=byid.get(dep)
        if not b or b['status']!='published' or not isinstance(b['github']['number'],int):
            raise GateError(f'{cid}: unresolved dependency {dep}')
        dep_issue=client.issue(b['github']['number'])
        if dep_issue.get('state')!='closed':raise GateError(f'{cid}: dependency not closed: {dep}')
    results=[]
    for bid,b,n in [(uid,ub,ub['github']['number']),(cid,binding,number)]:
        metadata=b.get('execution_approval') or {}
        revision=metadata.get('scope_revision')
        if not revision:raise GateError(f'{bid}: scope revision missing')
        digest=canonical_scope_hash(bid)
        evidence=approval(client.comments(n),bid,revision,digest,approvers)
        results.append({'local_id':bid,**evidence})
    sha=subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,capture_output=True,text=True)
    if sha.returncode!=0:raise GateError('Commit baseline unavailable')
    return {'schema_version':'1.0','status':'APPROVED_FOR_RUN','canonical_child_id':cid,'umbrella_id':uid,'milestone_id':mid,'issue_number':number,'engine':engine,'provider':'github','repository':repo,'base_sha':sha.stdout.strip(),'scope_evidence':results,'dispatch_authorized':True}


def main():
    p=argparse.ArgumentParser();p.add_argument('--issue-number',type=int,required=True);p.add_argument('--engine',choices=['opencode','mini-swe'],required=True);p.add_argument('--out',required=True)
    a=p.parse_args()
    repo=os.environ.get('GITHUB_REPOSITORY','')
    allowed={x.strip().casefold() for x in os.environ.get('BYAR_HUMAN_APPROVERS','').split(',') if x.strip()}
    try:
        client=GitHubRead(repo,os.environ.get('GITHUB_TOKEN'))
        r=preflight(a.issue_number,a.engine,repo,allowed,client)
        dest=Path(a.out);dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'status':'PASS','child':r['canonical_child_id'],'engine':r['engine'],'scope_evidence':r['scope_evidence']},ensure_ascii=False))
    except (GateError,ValueError,KeyError) as e:
        print(json.dumps({'status':'BLOCKED','reason':str(e)},ensure_ascii=False),file=sys.stderr)
        return 1
    return 0
if __name__=='__main__':sys.exit(main())
