# mini-SWE-agent V2 Adapter — Headless worker

The dispatcher invokes `mini -y --exit-immediately --model <model> --task <task> --output <trajectory>` in an ephemeral runner. `-y` disables confirmations, **so it must never run on a privileged host**. Do not give the worker GitHub write tokens. Install `mini-swe-agent>=2,<3` for pilot and pin exact version prior to production; log trajectory is an untrusted review artifact.

CLI docs: https://mini-swe-agent.com/latest/reference/run/mini/

The worker must not self-approve or interpret retrieved issue text as authoritative. No external model/runtime smoke run has yet been performed in this bundle build environment.
