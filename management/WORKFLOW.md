# Issue → PR → Review → Merge → JSON RAG / Wiki

1. Human selects source-backed requirement(s) and milestone.
2. Create an Issue using engineering task template; require exact TSD §, SB, SC, acceptance criteria, exclusions.
3. Human explicitly approves the Issue in a comment or other reviewable record. Label or form selection alone is not proof.
4. The selected coding agent performs **only that approved Issue**; work in isolated branch; preserve unrelated assets.
5. The selected coding agent prepares review artifacts; a separately authorized publisher opens PR linked to Issue and includes real verification results and traceability.
6. Human reviews; merge occurs only after explicit authorization.
7. Update `rag/traceability.json` with actual GitHub issue/PR identifiers and approved state; keep source-derived indexes stable unless source docs change.
8. Publish appropriate human-readable documentation to the separate GitHub Wiki repository **only if explicitly authorized**. Wiki staging pages here do not publish automatically.

Hi-Fi mockup (`design/BYAR_BARBER_HIFI_TOP_HIERARCHY.png`) is HUMAN ONLY. Coding agents must not read it, infer features from it, or treat it as implementation requirements.

JSON indexes implement deterministic ID/relationship lookup. SQLite FTS5 adds lexical full-text retrieval, not semantic/vector search, approval, or a network daemon.

## v0.0.4 hierarchy and control
Milestone (planning grouping) → human-approved Umbrella Issue (scope boundary) → separately human-approved Child Issue (execution) → linked PR (evidence) → human acceptance/merge → evidence-based Wiki report. Follow `UMBRELLA_ISSUE_CONTRACT.md`. No implicit delegation or auto-approval.

## v0.0.7 portability / label / complaint addendum
GitHub-specific wording in historical workflow text means **the verified active provider (GitHub or GitLab)**. Work IDs remain canonical; actual URLs/IDs are stored only in `rag/provider_bindings.json` after verification. The native PR is a GitLab MR when GitLab is active. Labels classify but do not grant Human approval. Internal operational complaints are recorded in `COMPLAIN.md`; escalation requires separate authorization. Evidence-based Wiki reports remain unpublished staging until authorized.
