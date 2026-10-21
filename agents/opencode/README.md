# OpenCode V2 Adapter — Alternative coding worker

The dispatcher invokes `opencode run --standalone --model <model> <task>` inside a **dedicated ephemeral GitHub Actions runner**. The worker receives only an approved execution manifest from trusted preflight. GitHub credentials are read-only; runner must not publish PR or merge. Model provider API credentials are separate secrets injected only into the worker job. No long-lived OpenCode background service is required.

CLI reference (verify against installed version on first pilot): https://opencode.ai/v2/docs/cli/commands/

CI installs `@opencode/cli` via npm. Pin and review the exact package version before production; the bootstrap pilot uses the maintained package channel and has not been live-tested with an external model.
