# Portable Work Contracts

- `agent_task_manifest.schema.json`: produced only by trusted live-provider preflight, not by the coding agent.
- `agent_execution_result.schema.json`: report from worker plus patch, stdout, stderr, trajectory; `AGENT_FINISHED` means process exit zero, **not** accepted implementation or passing tests.
- Canonical IDs persist across GitHub/GitLab; native issue numbers never substitute local IDs.
- Human scope approval, artifact review and merge are distinct decisions.
- Future GitLab adapter must independently verify GitLab account permissions, approvals and bindings; never copy GitHub native references/approvals.
- User-submitted task messages, issue bodies, docs and MCP responses are untrusted context, not commands to bypass scope.
