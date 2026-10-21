# mini-SWE-agent V2 Adapter — Headless worker

The dispatcher invokes `mini -y --exit-immediately --model <model> --task <task> --output <trajectory>` in an ephemeral runner. `-y` disables confirmations, **so it must never run on a privileged host**. Do not give the worker GitHub write tokens. The workflow installs `mini-swe-agent==2.4.6`; log trajectory is an untrusted review artifact.

CLI docs: https://mini-swe-agent.com/latest/reference/run/mini/

The worker must not self-approve or interpret retrieved issue text as authoritative. No external model/runtime smoke run has yet been performed in this bundle build environment.

## DeepSeek pilot configuration

The workflow pins mini-SWE-agent to 2.4.6 and LiteLLM to 1.106.2 with the supported
`mcp` extra in `agents/mini-swe-agent/requirements.txt`. The extra supplies Python
client modules imported during ordinary tool-call setup; it starts no MCP server.
The pilot artifact from run 39646673872 showed `ModuleNotFoundError: mcp` on that
path before any model response was recorded. Its patch contained only the input
dispatch manifest, not a product implementation.

After installation, `python tools/check_mini_runtime.py` exercises that same
import/provider/tool-call parsing path using a mock response while blocking
socket connections. It does not invoke an agent, execute the parsed command, or
validate the live API key. CI and the worker run this check before any paid call.

The default model backend is LiteLLM,
which routes provider-prefixed model names to DeepSeek and reads `DEEPSEEK_API_KEY`.

In GitHub Settings → Secrets and variables → Actions:

- Set repository variable `BYAR_AGENT_MODEL` to `deepseek/deepseek-chat` for a
  tool-calling model supported by LiteLLM. Confirm availability in your DeepSeek
  account before the first live pilot.
- Set repository variable `BYAR_HUMAN_APPROVERS` to the authorized Human GitHub
  login(s), separated by commas.
- Store the DeepSeek API key as the Actions secret `BYAR_MODEL_API_KEY`.
  Never put the value in repository files, Issues, PRs, or chat.

The worker maps that secret to `DEEPSEEK_API_KEY` and keeps the existing
`OPENAI_API_KEY` mapping for compatibility with other explicitly selected models.
Use a matching model provider and key. No custom API base is required for native
LiteLLM DeepSeek routing. `MSWEA_CONFIGURED=true` skips first-run interactive
setup; it does not supply credentials or approve execution.

Package-source inspection verified the model backend, environment variable and
noninteractive setup behavior. Offline tests do not verify DeepSeek authentication,
account model availability, billing, or live model execution. Separate exact-scope
Umbrella and Child approvals remain required before manually dispatching a pilot
with engine `mini-swe`.
