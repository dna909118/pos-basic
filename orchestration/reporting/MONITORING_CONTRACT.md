# Evidence-only Monitoring Contract

Control view: GitHub Projects + Actions for initial pilot; `wiki/` contains staged Markdown, not automatically published remote Wiki. Metrics are `not_collected` absent provider evidence. Execution job statuses are `QUEUED`, `PREFLIGHT_BLOCKED`, `RUNNING`, `ARTIFACT_READY`, `FAILED`, `UNDER_HUMAN_REVIEW`, `ACCEPTED` (Human evidence only). Do not derive `ACCEPTED` from agent exit code.

Every run should correlate canonical Child ID, GitHub repository/Issue number, GitHub Actions run URL, selected engine, exact commit, parent/child scope evidence, tests executed, artifact digest, PR (if separately published), and Human review decision. No fictitious timestamps, costs, test passes, or Wiki links.
