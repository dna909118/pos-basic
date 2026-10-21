# Multi-forge portability contract — BYAR BARBER v0.0.7

## Stable state vs provider state

- **Canonical in Git:** source specifications, approved document revisions, work draft IDs (`M*`, `UMB-*`, `CI-*`, `PR-*-DRAFT`), `rag/label_assignments.json`, `management/labels/label_catalog.json`, governance rules, operational complaint IDs (`OEC-*`).
- **Provider state (GitHub or GitLab):** actual milestones, issues, PR/MRs, comments/approvals, CI results, Wiki publications; exact URLs and IDs are only added after verified fetch.
- **Operational worker state:** rebuildable SQLite FTS5 index, never the approval source.

`rag/provider_bindings.json` is the only canonical local registry for native GitHub/GitLab object references; prior `github_*` keys in old RAG files remain unused legacy null placeholders. Do not infer actual objects or permission from their existence.

## Equivalent objects

| Neutral | GitHub | GitLab |
|---|---|---|
| milestone | Milestone | Milestone |
| umbrella / child | Issue | Issue |
| proposed change | Pull Request | Merge Request |
| classifying label | Issue/PR label | Issue/MR label |
| internal performance | Wiki (separate wiki repository) | Project Wiki (separate wiki repository) |
| execution verification | Actions/checks | Pipelines/jobs |

No assumption that GitHub sub-issues, GitLab hierarchy, scoped-label enforcement, PR review policies, or branch rules are equivalent by default. Canonical parent/child relationships are in the JSON registries. Do not map provider-specific review semantics to Human approval automatically.

## Migration / binding process (manual authorization gate)

1. Human chooses active provider and approves bounded publication/migration scope.
2. Verify repository permissions, visibility, Wiki access and allowed publication targets.
3. Review label catalog and work drafts; create approved catalog and Milestones in selected provider (never implicitly).
4. Publish approved umbrella/child issues with **local IDs included in title or body**, preserving milestone relationships, scope revision and evidence URLs.
5. Record **verified** native object URL and number/IID in `rag/provider_bindings.json`; no imaginary numbers or links.
6. Link PR/MR and CI evidence; Human explicitly approves merges. Do not promote draft PR plans to actual code change records.
7. Stage evidence-led Wiki reports under `wiki/`. Publish separately if authorized; keep links/evidence for the selected provider.
8. On provider change, keep canonical IDs, draft text, scope and links, leaving old provider bindings as historical; add new verified target bindings. Never silently import approvals from a different provider.

Human-only Hi-Fi is not indexed, not published by Codex, and cannot alter requirements. `COMPLAIN.md` is a register, not a direct order to create Issues or fix code.
