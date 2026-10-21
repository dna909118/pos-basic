# BYAR BARBER — Engineering Bootstrap Bundle v0.0.8

This is a **portable, reviewable GitHub/GitLab engineering work bundle**, not a running Flutter app, a published Wiki, or created Issues/PRs/MRs. Changes in this version build on v0.0.6 without modifying TSD, UX Storyboard, Lo-Fi, Design System, or the Human-only Hi-Fi image.

## Concrete draft inventory
- 7 **Milestone drafts**: `management/drafts/milestones/`.
- 7 **Umbrella Issue drafts**: `management/drafts/umbrellas/`.
- 40 **Child Issue drafts**: `management/drafts/issues/` (36 from storyboard, 4 engineering prerequisites).
- 7 **PR/MR planning drafts**: `management/drafts/pull_requests/` (NOT actual PR/MRs).
- **47 populated label assignments** (7 Umbrella + 40 Child): `rag/label_assignments.json`, with human-untriaged priority and approval-required workflow states.
- Canonical **label catalog** and provider-specific label creation draft payloads under `management/labels/` and `management/providers/`.
- **61 provider binding draft entries** (7+7+40+7) in `rag/provider_bindings.json`, all GitHub/GitLab references empty until verified.
- **COMPLAIN.md** with an empty real-incident register; `rag/complaints.json` (zero *recorded* entries, provider state unknown) and escalation lifecycle.

## Engineering authority & retrieval
Human controls Milestone approval, Umbrella scope revisions, Child task authorization, PR/MR review/merge, complaint escalation, labels publication, and Wiki publication. **No label, complaint or RAG match substitutes Human approval.** Native provider state is derived from verified GitHub/GitLab objects, never invented from draft IDs. `management/PORTABILITY_CONTRACT.md` maps both forges; `AGENTS.md` is the Codex guardrail.

Git-versioned Markdown and JSON are persistent knowledge. `rag/fts5/operational_index.py` builds a lexical SQLite FTS5 index offline in each worker; the runtime database is gitignored. No embedding, external model download, or semantic search is used. Results are context only, never approval evidence.

Hi-Fi at `design/BYAR_BARBER_HIFI_TOP_HIERARCHY.png` remains **HUMAN ONLY**; it is never a Codex input.

## Draft publishing / validation
1. Run `python tools/validate_governance.py` locally or in an isolated worker to check offline label and work draft structure.
2. Human reviews appropriate Milestone, Umbrella/Child drafts and authorizes what may be published in chosen provider.
3. Use native `.github/` or `.gitlab/` templates, preserving canonical IDs. Provider label catalogs are draft payloads only, NOT executed API changes.
4. Populate verified references in `rag/provider_bindings.json` after actual creation; never invent remote links or infer approval from registry presence.
5. Human reviews PR/MR and publishes evidence-based Wiki reports only when explicitly approved.

Current known limits: there is no provider API synchronization/enforcement, no live CI evidence or Wiki publication, no Flutter implementation, and no live provider approval or agent/API integration run. Complaint counts are only locally registered counts.

## v0.0.8 clean repository bootstrap (no existing provider objects assumed)
1. Unzip into a new empty repository working tree. Preserve historical v0.0.7 archive separately; never overwrite an active main branch with this bundle.
2. Run `python tools/validate_governance.py`, `python -m unittest discover -s tests -v`, `python rag/fts5/operational_index.py build`, and `python rag/fts5/operational_index.py status`.
3. Commit accepted source to Git. Runtime `rag/runtime/` must remain untracked. Configure `GITHUB_REPOSITORY` at CI runtime; provider IDs intentionally remain null until objects are actually created and verified.
4. Publication of 35 labels, M01-M07, Umbrella and Child draft Issues requires separate Human authorization and provider binding synchronization. No work runs until authorized scope comments and exact draft hashes pass live preflight.
5. `.github/workflows/engineering-validation.yml` runs offline checks; `.github/workflows/agent-dispatch.yml` is a manual, fail-closed, artifact-only worker pilot. See `orchestration/README.md`. No auto-publish or auto-merge.
6. OpenCode V2 and mini-SWE-agent V2 are alternative workers. Hermes is excluded. MCP schema is an optional integration contract, not a running server. Flutter business app is not included.

## Flutter builder (v0.0.8-r1)
The Flutter **web builder toolchain and GitHub Actions build workflow are preconfigured** under `builder/flutter/`, `tools/flutter_builder.py`, and `.github/workflows/flutter-builder.yml`. A disposable smoke Flutter project verifies toolchain + Mix + web compilation; when an approved application exists under `app/`, the same CI path compiles and publishes its web-build artifact. No product UI/application code is bundled. Actual Flutter build and CI must still be verified on a live runner. See `builder/flutter/README.md`.

## GitHub Free Private baseline (v0.0.8-r2)
Configured target is `dna909118/pos-basic` (repository state is **not** verified by this archive). Account stays GitHub **Free**, repo **private**, mode **soft_governance**. Required Human review, CI checks, and avoiding direct pushes to `main` are procedural controls only: native branch protection/rulesets cannot enforce them at this tier. Keep manual agent dispatch with read-only credentials, explicit live approval preflight, artifacts for Human review and no agent merge. See `management/providers/GITHUB_FREE_PRIVATE_GOVERNANCE.md`. No public visibility, paid upgrade, hard-protection claim or provider mutation is included.
