#!/usr/bin/env python3
"""Offline contractual checks for GitHub Free private soft governance."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = "management/providers/github_free_private_policy.json"
EXPECTED_NATIVE_FIELDS = (
    "branch_protection_available", "repository_rulesets_available",
    "required_status_checks_enforced", "required_pr_review_enforced",
    "direct_push_blocked_by_platform", "required_human_approval_enforced_by_platform"
)
EXPECTED_OPERATING_FIELDS = (
    "human_review_required_by_process", "human_merge_required_by_process",
    "manual_agent_dispatch_only", "agent_artifact_only",
    "live_human_and_scope_approval_preflight", "ci_required_by_process_not_platform"
)


def load_policy(root=ROOT):
    return json.loads((root / POLICY_PATH).read_text(encoding="utf-8"))


def validate_policy(policy, workflow):
    issues = []
    def check(ok, message):
        if not ok:
            issues.append(message)
    check(policy.get("schema_version") == "1.0", "Unknown soft-governance policy schema")
    check(policy.get("active_provider") == "github", "Active provider must be GitHub")
    check(policy.get("target_repository") == "dna909118/pos-basic", "Unexpected repository target")
    check(policy.get("github_plan") == "free", "GitHub plan must remain Free")
    check(policy.get("repository_visibility") == "private", "Visibility must remain private")
    check(policy.get("protection_mode") == "soft_governance", "Only soft governance is available")
    check(policy.get("gitlab_portability_target") is True, "GitLab portability must be retained")
    native = policy.get("native_enforcement", {})
    for name in EXPECTED_NATIVE_FIELDS:
        check(native.get(name) is False, f"Unsupported native hard enforcement claimed: {name}")
    ops = policy.get("operational_controls", {})
    for name in EXPECTED_OPERATING_FIELDS:
        check(ops.get(name) is True, f"Required procedural control missing: {name}")
    for name in ("automatic_merge_authorized", "agent_repository_write_authorized"):
        check(ops.get(name) is False, f"Unsafe operational control: {name}")
    # This protects the distributed workflow as a *release policy*; it is not a native
    # GitHub permission enforcement or a complete YAML parser.
    check("workflow_dispatch:" in workflow, "Manual workflow dispatch missing")
    check("permissions:\n  contents: read\n  issues: read" in workflow,
          "Global workflow token permissions must be read-only")
    check("permissions:\n      contents: read" in workflow,
          "Agent worker must have contents:read only")
    check("persist-credentials: false" in workflow, "Checkout credential persistence must be disabled")
    check("orchestration/governance_gate/preflight.py" in workflow,
          "Online governance preflight must remain in workflow")
    check("actions/upload-artifact" in workflow, "Artifact-only review output missing")
    for pattern in (r"(?m)^\s*contents:\s*write\s*$", r"(?m)^\s*pull-requests:\s*write\s*$",
                    r"(?m)^\s*issues:\s*write\s*$"):
        check(re.search(pattern, workflow) is None, "Write-token permission found")
    for pattern in ("gh pr create", "gh pr merge", "git push", "pull_request_target:", "issues:\n", "issue_comment:"):
        check(pattern not in workflow, f"Unapproved workflow automation: {pattern}")
    return issues


def expected_repository(repo, policy):
    return bool(repo and repo == policy.get("target_repository")
                and policy.get("active_provider") == "github"
                and policy.get("github_plan") == "free"
                and policy.get("repository_visibility") == "private"
                and policy.get("protection_mode") == "soft_governance")
