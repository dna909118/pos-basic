# Wiki Reporting Contract — Internal Engineering Performance

## Purpose and provenance
Wiki is the human-facing **internal performance report**, separate from normative TSD and governance approvals. GitHub milestones, approved umbrella issues, child issues, PRs, review records and CI runs are evidence sources; JSON indexes are lookup aids only.

## Reporting pages
- `Engineering-Dashboard.md`: high-level verified KPIs and evidence links.
- `Milestone-Performance.md`: one section per milestone and parent umbrella.
- `Umbrella-Issue-Register.md`: scope revision, parent state, approval, child count, blockers.
- `Execution-Progress.md`: approved children, linked PRs and acceptance state.
- `Quality-CI-Report.md`: observed format/analyze/test/build results and URLs.
- `Engineering-Decision-Log.md`: approved human decisions and source links.

## Update policy
1. Fetch real GitHub evidence and record retrieval timestamp plus URLs; do not synthesize live status from proposals.
2. Proposed or missing information is `not_created`, `not_collected`, `unknown` or `pending_approval` (as appropriate), never a fabricated numeric zero.
3. Distinguish `planned`, `approved`, `in_progress`, `blocked`, `review`, `accepted`, `closed`; map to actual linked evidence.
4. Exclude screenshot Hi-Fi from Codex implementation context; human may review it separately.
5. Stage changes in repository Wiki folder; publishing to GitHub Wiki requires explicit human authorization (Wiki has a separate repository).
6. Record report timestamp, source link, responsible reviewer, unverified limitations and method used for any percentage.
7. Wiki never authorizes child tasks, closes issues or replaces PR review.

## v0.0.7 portability / label / complaint addendum
GitHub-specific wording in historical workflow text means **the verified active provider (GitHub or GitLab)**. Work IDs remain canonical; actual URLs/IDs are stored only in `rag/provider_bindings.json` after verification. The native PR is a GitLab MR when GitLab is active. Labels classify but do not grant Human approval. Internal operational complaints are recorded in `COMPLAIN.md`; escalation requires separate authorization. Evidence-based Wiki reports remain unpublished staging until authorized.
