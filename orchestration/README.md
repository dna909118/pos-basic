# Agent dispatch on clean GitHub bootstrap (manual pilot)

This is a **fail-closed, artifact-only pilot**. No automatic issue creation, scheduled queue, workflow label trigger, PR publisher, merger, deployment or GitLab execution backend is included. Existing governance drafts remain unpublished until separate Human authorization. GitHub Actions + model execution require network, repository settings, provider credentials and a live approved Issue. Tests executed offline cannot attest to those external integrations.

## Repository initialization order

1. Merge accepted source into a newly initialized repository `main`. Do not re-import old provider numbers, PRs or execution approvals. Keep historical GitHub repository data out of the clean bundle.
2. `python tools/validate_governance.py`, `python -m unittest discover -s tests -v`, then FTS5 `build/status/query/lookup`.
3. After explicit Human approval, publish labels and Milestone/Issue drafts; verify exact GitHub IDs and URLs; fill `rag/provider_bindings.json` (status `published`, provider refs complete) through an authorized PR. Do not delete or rewrite canonical IDs.
4. In GitHub repository settings, configure `BYAR_HUMAN_APPROVERS` as a repository **variable** containing explicitly authorized GitHub logins separated by commas. These must not be bot accounts.
5. Set `BYAR_AGENT_MODEL` as a repository variable for the chosen engine. Set `BYAR_MODEL_API_KEY` in GitHub **Secrets** for the model provider. The included workflow uses `OPENAI_API_KEY`; adapt the worker environment deliberately if using another provider. The account's ChatGPT subscription is not an API key.
6. For each approved parent and child issue, Human writes a **standalone full-line** comment in its GitHub Issue (not the PR):

   `BYAR-APPROVE UMB-M01 revision=draft-1 sha256=<64-hex SHA256 of management/drafts/umbrellas/UMB-M01.md>`

   `BYAR-APPROVE CI-F01 revision=draft-1 sha256=<64-hex SHA256 of management/drafts/issues/CI-F01.md>`

   Compute using `sha256sum <exact-file>`. Child issue comment is separate from its Umbrella. To revoke, add `BYAR-REVOKE <ID> revision=<revision> sha256=<digest>` as later comment. Changed source bytes invalidate previous approval automatically. Only comments from logins in the allowlist count. No approval if any required live lookup fails.
7. Human goes to Actions → **BYAR BARBER Manual Agent Pilot** → Run Workflow, enters actual verified GitHub Issue number and `opencode` or `mini-swe`.
8. `preflight` checks active provider, published bindings, parent/child relationship, exact scope hashes, Human comment identity, issue/Milestone association and closed dependencies (only if `depends_on` is explicitly registered). It writes a manifest ONLY if all pass; if not, workflow stops before agent.
9. Ephemeral `worker` uses sparse checkout excluding `design/` (Human-only Hi-Fi is not available in its workspace), downloads the manifest, checks commit, rebuilds FTS5, runs agent, uploads review-only logs/patch/trajectory. No push, PR, merge, issue closure, or Wiki publish. Run separate code review, tests and provenance/security checks before approving any patch. **Agent cannot approve its own patch.**

## Operating limits

- Approval is not inferred from a label, Issue status, PR, JSON, agent message or MCP response. The Human approval protocol is specified here, not a built-in GitHub authorization feature. GitHub Free private does not provide full policy enforcement for all Human rules.
- GH Actions concurrency serializes requested issue runs but does not guarantee persistent cross-workflow idempotency or prevent manual PR duplication. Deploy a persistent dispatcher before enabling automatic queues.
- Model execution can run arbitrary repository code; GitHub-hosted runner is ephemeral but cannot protect an injected inference API key from malicious task code. Audit trust boundaries, install version pins, and consider stronger sandbox/network control before broad automation.
- Worker stdout, patches and trajectories can contain sensitive data: keep repository private, inspect artifacts before redistribution, and use minimum retention.
- GitHub hosted runner minutes, model inference charges, and Actions concurrency limits apply.
- `AGENT_FINISHED` and CI green do not prove Human acceptance. The worker intentionally does not publish PR.
- `BYAR_HUMAN_APPROVERS` is an operator-configured allowlist, not a substitute for provider authentication; the actual live GitHub comment author is verified by API.
