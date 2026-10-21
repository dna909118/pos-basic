# SQLite FTS5 Operational Retrieval

Rebuildable lexical index: **no embeddings, model downloads, ChromaDB or external network**. All source documents/JSON are versioned persistent knowledge; `rag/runtime/knowledge.sqlite3` is derived, gitignored, and never authority for execution.

```bash
python rag/fts5/operational_index.py build
python rag/fts5/operational_index.py status
python rag/fts5/operational_index.py query "pembayaran DP pelunasan" --top-k 5
python rag/fts5/operational_index.py lookup CI-F01
python rag/fts5/operational_index.py lookup REF-SB-16
```

`status` fails closed for missing, corrupt, invalid schema, stale, or altered source snapshots. Unicode61/BM25 search is **lexical**: do not present it as semantic ranking. `lookup` returns exact canonical JSON records, not Human approval. Configuration: `config.json`. Directory and human-only exclusions are mandatory. Rebuild in each clean GitHub Actions job after checkout.
