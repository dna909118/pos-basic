"""Offline, standard-library integrity and governance tests."""
import importlib.util
import json
import sqlite3
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
def import_script(name,relative):
    spec=importlib.util.spec_from_file_location(name,ROOT/relative)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m

fts=import_script('bb_fts','rag/fts5/operational_index.py')
gate=import_script('bb_gate','orchestration/governance_gate/preflight.py')
worker=import_script('bb_worker','orchestration/dispatcher/run_agent.py')
validator=import_script('bb_validator','tools/validate_governance.py')

class FTS5Tests(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory()
        self.addCleanup(self.t.cleanup)
        self.root=Path(self.t.name)
        (self.root/'rag/fts5').mkdir(parents=True)
        (self.root/'rag/runtime').mkdir(parents=True)
        (self.root/'docs').mkdir()
        (self.root/'design').mkdir()
        (self.root/'docs/example.md').write_text('Pembayaran DP pelunasan\nPontianak dan ë Unicode\n',encoding='utf-8')
        (self.root/'design/secret.md').write_text('DO NOT INDEX THIS',encoding='utf-8')
        cfg={'engine':'sqlite-fts5','index_sources':['docs','design'], 'exclude_paths':['design/','rag/runtime/'],'human_only':['design/secret.md'],'chunk_chars':60,'chunk_overlap':8,'local_path':'rag/runtime/knowledge.sqlite3'}
        (self.root/'rag/fts5/config.json').write_text(json.dumps(cfg),encoding='utf-8')
        self.patch=patch.object(fts,'ROOT',self.root);self.patch.start();self.addCleanup(self.patch.stop)
    def test_build_readiness(self):
        self.assertEqual(fts.build()['sources'],1)
        self.assertTrue(fts.validate_db()['ready'])
    def test_repeatable_build(self):
        a=fts.build();b=fts.build()
        self.assertEqual((a['sources'],a['chunks']),(b['sources'],b['chunks']))
    def test_unicode(self):
        fts.build();self.assertTrue(fts.search('Pontianak ë',3))
    def test_bm25_payment(self):
        fts.build();self.assertIn('docs/example.md',[x['source'] for x in fts.search('DP pelunasan')])
    def test_reject_fts_syntax_injection(self):
        fts.build();self.assertEqual(fts.search('" OR NOT *'),[])
    def test_reject_empty(self):
        fts.build()
        with self.assertRaises(ValueError):fts.search('  ')
    def test_stale_source(self):
        fts.build();(self.root/'docs/example.md').write_text('content changed')
        self.assertEqual(fts.validate_db()['reason'],'stale_sources')
    def test_missing(self):
        self.assertEqual(fts.validate_db()['reason'],'missing_index')
    def test_corrupt(self):
        fts.build();(self.root/'rag/runtime/knowledge.sqlite3').write_bytes(b'broken')
        self.assertFalse(fts.validate_db()['ready'])
    def test_human_only_excluded(self):
        self.assertEqual(fts.source_files(fts.configuration()),['docs/example.md'])
    def test_bad_runtime_location_rejected(self):
        cfg=fts.configuration();cfg['local_path']='design/knowledge.sqlite3'
        with self.assertRaises(ValueError):fts.db_path(cfg)

class CanonicalTests(unittest.TestCase):
    def test_governance_structural_pass(self):
        problems,summary=validator.validate();self.assertFalse(problems,problems)
        self.assertEqual((summary['children'],summary['provider_bindings']),(40,61))
    def test_id_lookup(self):
        got=fts.lookup('REF-SB-16')
        self.assertEqual(got[0]['record']['title'],'Menyelesaikan pembayaran')
    def test_draft_hash(self):
        self.assertEqual(len(gate.canonical_scope_hash('CI-F01')),64)
    def test_unknown_draft_rejected(self):
        with self.assertRaises(gate.GateError):gate.canonical_scope_hash('CI-INVALID')
    def test_no_local_approval(self):
        x=gate.load('rag/provider_bindings.json')
        self.assertEqual(x['active_provider'],'github')
        # Provider publication is distinct from authorization to execute work.
        for binding in x['bindings']:
            if binding['kind'] not in ('umbrella', 'child'):
                continue
            approval = binding['execution_approval']
            self.assertEqual(approval['state'], 'pending_approval')
            for key in ('approved_scope_revision', 'approved_scope_sha256',
                        'evidence_url', 'approved_by', 'verified_at', 'provider'):
                self.assertIsNone(approval[key], (binding['local_id'], key))

class ApprovalTests(unittest.TestCase):
    def setUp(self):
        self.h='a'*64
    def comment(self,verb='APPROVE',actor='the-human',rev='draft-1',hash=None,when='2026-10-21T10:00:00Z'):
        return {'user':{'login':actor,'type':'User'},'body':f'BYAR-{verb} CI-F01 revision={rev} sha256={hash or self.h}','created_at':when,'id':1,'html_url':'https://github.com/example/repo/issues/3#issuecomment-1'}
    def test_valid_exact(self):
        result=gate.approval([self.comment()],'CI-F01','draft-1',self.h,{'the-human'})
        self.assertEqual(result['approved_by'],'the-human')
    def test_wrong_actor(self):
        with self.assertRaises(gate.GateError):gate.approval([self.comment(actor='bot')],'CI-F01','draft-1',self.h,{'the-human'})
    def test_stale_hash(self):
        with self.assertRaises(gate.GateError):gate.approval([self.comment(hash='b'*64)],'CI-F01','draft-1',self.h,{'the-human'})
    def test_revoked(self):
        with self.assertRaises(gate.GateError):gate.approval([self.comment(),self.comment(verb='REVOKE',when='2026-10-21T11:00:00Z')],'CI-F01','draft-1',self.h,{'the-human'})
    def test_never_authorized_from_clean_bundle(self):
        class Fake:
            def issue(self,n):
                return {'number':n,'state':'open','title':'[CI-F01] pilot','html_url':'https://github.com/a/b/issues/3'}
        with self.assertRaises(gate.GateError):gate.preflight(3,'opencode','a/b',{'the-human'},Fake())

class WorkerTests(unittest.TestCase):
    def test_reject_unauthorized_manifest(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'m.json';p.write_text(json.dumps({'status':'DRAFT','dispatch_authorized':False}))
            with self.assertRaises(ValueError):worker.run(p,Path(d)/'result','openai/example',dry_run=True)
    def test_valid_manifest_dry_run(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d);p=r/'m.json'
            p.write_text(json.dumps({'status':'APPROVED_FOR_RUN','dispatch_authorized':True,'provider':'github','engine':'mini-swe','canonical_child_id':'CI-F01','umbrella_id':'UMB-M01','milestone_id':'M01','repository':'a/b','issue_number':3,'base_sha':'a'*40,'scope_evidence':[{'x':1},{'x':2}]}))
            result=worker.run(p,r/'outputs','openai/example',dry_run=True)
            self.assertEqual(result['status'],'NOT_RUN')
            self.assertTrue((r/'outputs/execution_result.json').is_file())

if __name__=='__main__':unittest.main()

class MoreGateTests(unittest.TestCase):
    def test_non_open_issue_rejected(self):
        with self.assertRaises(gate.GateError):
            gate.verify_issue({'number':4,'state':'closed','title':'[CI-F01] test','repository_url':'https://api.github.com/repos/a/b'},'CI-F01',4,'a/b')
    def test_pr_not_issue_rejected(self):
        with self.assertRaises(gate.GateError):
            gate.verify_issue({'number':4,'state':'open','title':'[CI-F01] test','pull_request':{},'repository_url':'https://api.github.com/repos/a/b'},'CI-F01',4,'a/b')
    def test_missing_allowed_human_rejected(self):
        class Fake: pass
        with self.assertRaises(gate.GateError):
            gate.preflight(3,'mini-swe','a/b',set(),Fake())
    def test_bad_revision_rejected(self):
        h='a'*64
        comment={'user':{'login':'human','type':'User'},'body':'BYAR-APPROVE CI-F01 revision=draft-old sha256='+h,'created_at':'2026-01-01T00:00:00Z','id':1}
        with self.assertRaises(gate.GateError):
            gate.approval([comment],'CI-F01','draft-1',h,{'human'})
    def test_open_code_dry_run(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'m.json'
            p.write_text(json.dumps({'status':'APPROVED_FOR_RUN','dispatch_authorized':True,'provider':'github','engine':'opencode','canonical_child_id':'CI-F01','umbrella_id':'UMB-M01','milestone_id':'M01','repository':'a/b','issue_number':3,'base_sha':'a'*40,'scope_evidence':[{'x':1},{'x':2}]}))
            self.assertEqual(worker.run(p,Path(d)/'result','openai/example',dry_run=True)['status'],'NOT_RUN')

class SourceContainmentTests(unittest.TestCase):
    def test_no_parent_path_traversal(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);cfg={'index_sources':['../.env'],'exclude_paths':[],'human_only':[]}
            with patch.object(fts,'ROOT',root):
                with self.assertRaises(ValueError):fts.source_files(cfg)
