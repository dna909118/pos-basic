"""Tests that Free/private repo cannot be represented as hard branch-enforced."""
import importlib.util
import unittest
from copy import deepcopy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('byar_github_free_policy', ROOT/'tools/github_free_policy.py')
policy_mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy_mod)

class GithubFreePrivatePolicyTests(unittest.TestCase):
    def setUp(self):
        self.policy=policy_mod.load_policy()
        self.workflow=(ROOT/'.github/workflows/agent-dispatch.yml').read_text(encoding='utf-8')

    def test_clean_policy_and_read_only_workflow(self):
        self.assertEqual(policy_mod.validate_policy(self.policy,self.workflow),[])

    def test_repo_target_rejects_old_or_unexpected_repo(self):
        self.assertTrue(policy_mod.expected_repository('dna909118/pos-basic',self.policy))
        self.assertFalse(policy_mod.expected_repository('dna909118/barber-pro',self.policy))
        self.assertFalse(policy_mod.expected_repository('owner/fork',self.policy))

    def test_hard_branch_enforcement_claim_rejected(self):
        candidate=deepcopy(self.policy)
        candidate['native_enforcement']['branch_protection_available']=True
        self.assertTrue(policy_mod.validate_policy(candidate,self.workflow))

    def test_required_ci_claim_rejected(self):
        candidate=deepcopy(self.policy)
        candidate['native_enforcement']['required_status_checks_enforced']=True
        self.assertTrue(policy_mod.validate_policy(candidate,self.workflow))

    def test_upgrade_or_public_switch_rejected(self):
        for key,value in [('github_plan','pro'),('repository_visibility','public'),('protection_mode','hard_enforcement')]:
            with self.subTest(key=key):
                candidate=deepcopy(self.policy)
                candidate[key]=value
                self.assertTrue(policy_mod.validate_policy(candidate,self.workflow))

    def test_agent_write_permission_rejected(self):
        workflow=self.workflow.replace('      contents: read','      contents: write')
        self.assertTrue(policy_mod.validate_policy(self.policy,workflow))

    def test_live_preflight_refuses_wrong_repository_before_network(self):
        import importlib.util
        spec=importlib.util.spec_from_file_location('g_gate_check', ROOT/'orchestration/governance_gate/preflight.py')
        gate=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gate)
        class NoRequestsAllowed:
            def issue(self, n):
                raise AssertionError('Should not contact provider for wrong repo')
        with self.assertRaisesRegex(gate.GateError, 'Repository does not match'):
            gate.preflight(3,'mini-swe','dna909118/barber-pro',{'human'},NoRequestsAllowed())

    def test_automerge_procedure_rejected(self):
        candidate=deepcopy(self.policy)
        candidate['operational_controls']['automatic_merge_authorized']=True
        self.assertTrue(policy_mod.validate_policy(candidate,self.workflow))

    def test_missing_live_preflight_rejected(self):
        workflow=self.workflow.replace('orchestration/governance_gate/preflight.py','orchestration/governance_gate/skip.py')
        self.assertTrue(policy_mod.validate_policy(self.policy,workflow))

if __name__=='__main__': unittest.main()
