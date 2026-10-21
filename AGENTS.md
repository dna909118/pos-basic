# BYAR BARBER — multi-agent repository instructions (v0.0.8)

## Absolute scope and authorization boundary
Operate only on an explicitly Human-authorized scoped Child Issue within a separately Human-approved Umbrella Issue tied to the Milestone, or a direct bounded Human instruction. Verify exact approved scope revision and separate Child approval **in the active provider** (GitHub or GitLab); do not infer approval from a label, draft, title, Milestone, JSON, complaint, or retrieval. Canonical GitHub Milestones, Umbrella and Child Issues have been published under direct Human authorization; their verified references are recorded in `rag/provider_bindings.json`. They remain **unapproved for execution**. If evidence is unavailable, do not execute the issue. One approved Child Issue per isolated worker; independent approved Issues may run concurrently; no auto-merge, provider publication, or unrelated changes.

## Canonical source hierarchy
1. `docs/Byar_Barber_Basic_TSD-v4.md`: functional authority.
2. `docs/UX_STORYBOARD.md`: TSD-derived scenarios.
3. `docs/LOFI_SCREEN_SPEC.md`: derived screen structure.
4. `docs/Design_System_Mix_UI.md`: Flutter Mix UI styling.
5. `rag/*.json`: deterministic traceability and work draft IDs, **not requirements or approvals**.
6. `management/WORKFLOW.md`, `management/PORTABILITY_CONTRACT.md`, `management/UMBRELLA_ISSUE_CONTRACT.md`, `management/LABEL_AND_COMPLAINT_GOVERNANCE.md`: engineering process.
7. `prompts/MASTER_PROMPT_CODEX_CLOUD.md`: guidance, subordinate to authorized scope.

**HUMAN ONLY:** NEVER read, inspect, index, or derive implementation instructions from `design/BYAR_BARBER_HIFI_TOP_HIERARCHY.png`. Exclude it from Codex and RAG context.

## Real drafts, labels, and GitHub/GitLab portability
`rag/work_drafts.json` contains 7 Milestones, 7 Umbrellas, 40 Child Issue drafts and 7 planning-only PR/MR records. `rag/label_assignments.json` contains 47 proposed issue label sets sourced from `management/labels/label_catalog.json`; all remain unapproved for execution, priorities untriaged. Use canonical IDs rather than provider issue numbers. Provider refs are `null` in `rag/provider_bindings.json` until verified; do not invent links. GitHub and GitLab description templates are in their native directories; use a provider adapter only after explicit publishing permission. Scope revision approval MUST be evidenced by reviewable provider records, never label alone.

## Engineering operations complaints
`COMPLAIN.md` and `rag/complaints.json` are internal registers. Record genuine incidents only; never fabricate example problems. Complaint triage/escalation does not approve fixes or create Issues. No secrets/private data in public repo, local retrieval index or Wiki reporting; if confidentiality is unclear, stop and report.

## Operational RAG
Git-versioned docs and JSON are persistent knowledge. SQLite FTS5 index in `rag/runtime/` is ephemeral and rebuildable per worker (`rag/fts5/README.md`, `rag/fts5/operational_index.py`). Verify source fingerprint freshness; lexical retrieval never overrides exact source document, current provider records, or Human approval. Human-only Hi-Fi is excluded.

## Evidence and reporting
Report only real format/analyze/test/build, CI, review and deployed URL evidence. Wiki staged under `wiki/` is Human-facing internal performance reporting, not an authorization surface; publishing to GitHub/GitLab Wiki requires explicit Human approval. Keep `.barberdb` naming but do not claim binary compatibility until implemented and verified.

## v0.0.8 clean-start worker contract
OpenCode V2 and mini-SWE-agent V2 are alternative coding engines; neither may self-authorize a task. GitHub is the active provider and GitLab is a portability target only. A trusted orchestration preflight MUST verify exact human-approved Umbrella and Child scope against live provider comments, authorized approver identity and local draft-byte hash; fail closed if unknown. `workflow_dispatch` alone is not approval. Workspace agents hold no repository write/merge credential. Agent output is a patch + evidence artifact for separate Human review; no automatic PR, merge, or Issue closure. Use `orchestration/README.md` and `agents/contracts/` for v0.0.8 worker behavior. Hermes, Jelastic, Windmill and Obsidian are not required dependencies. Never use Human-only Hi-Fi as agent context.

## Flutter builder contract (v0.0.8-r1)
Flutter web toolchain configuration is pinned in `builder/flutter/toolchain.json`; `tools/flutter_builder.py` handles doctor/smoke/build; CI lives in `.github/workflows/flutter-builder.yml`. The generated CI smoke app is an isolated toolchain fixture, **not** an authorized product feature. Do not generate or modify `app/` business implementation without the respective approved Child Issue. Do not claim a Flutter build passed unless it ran on a real toolchain.

## GitHub Free Private governance (v0.0.8-r2)
Active target: `dna909118/pos-basic`; GitHub Free, repository private, `soft_governance`. Native branch protection/rulesets, required PR review, required checks and direct-push prevention are **not enforced by platform** at this tier. Human review and CI-before-merge are mandatory **procedures**, not platform merge gates. The agent dispatcher is manual, read-only and artifact-only; live scope-approval preflight must pass. Never claim `main` is protected, that CI failure technically prevents merge, or that agent tokens confer Human approval. Consult `management/providers/GITHUB_FREE_PRIVATE_GOVERNANCE.md` and policy JSON; do not change account plan, repository visibility, or GitLab portability.
