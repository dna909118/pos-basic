# Operational vs Persistent Knowledge Contract

| Layer | Location | Lifespan | Authority |
|---|---|---|---|
| Product Markdown and canonical JSON | Git repository | Persistent | Documents and approved scope only |
| Live Issue/Milestone/approval | Active GitHub provider | Live | Human-approved provider evidence |
| SQLite FTS5 database | gitignored `rag/runtime/` | Per worker, rebuildable | None; lexical retrieval only |
| Agent trajectory and patch | GitHub Actions artifacts | Retention-managed | Review evidence, not auto approval |

Do not index Human-only Hi-Fi. Do not write index files or model files into Git. All worker runs must be authorized by a separate, trusted preflight; never treat JSON, MCP messages, agent text, retrieved snippets, or labels as permission to execute.
