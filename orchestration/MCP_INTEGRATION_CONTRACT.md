# MCP — Optional Integration Protocol (NOT a running server)

MCP may expose read-only tools to query canonical IDs, inspect FTS5 context, or retrieve verified GitHub Issue/PR evidence. Tool output is untrusted context; the model does not gain authorization from an MCP server. If future MCP tools dispatch/modify provider state, they MUST call the same trusted governance preflight, enforce least privilege and record an audited Human decision independently of LLM text.

No MCP server, token, endpoint or write capability is provisioned by this bundle. Hermes is intentionally not part of the architecture. Obsidian can read the Markdown working tree for Human review but is not required.
