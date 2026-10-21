# Umbrella Issue Contract — BYAR BARBER v0.0.4

## Governance authority
- **Human Product Owner** approves an Umbrella Issue's scope, exclusions, acceptance criteria, authorized child issues, changes and closure in reviewable GitHub comments/decisions.
- **Milestone** groups delivery goals; assignment to a milestone **does not authorize work**.
- **Umbrella Issue** establishes the temporary authorization boundary. It is not blanket permission to work on every child.
- **Child Issue** is the executable unit only after human approval **and** explicit membership in a human-approved Umbrella Issue; no task execution for unapproved or unmatched children.
- **PR** must identify the executable child and umbrella, and provide test/build evidence. Merging always requires human approval.
- **Wiki** is an evidence-based internal performance reporting surface, not an approval source.
- **JSON RAG** stores deterministic references/relations, never grants authority or invents GitHub IDs.

## Required Umbrella fields
Milestone ID and actual URL (once created); umbrella Issue URL; owner/approver; exact authorized scope; TSD section(s) and related SB/SC IDs where applicable; permitted work classes; explicit exclusions; child issue register; entry/exit criteria; acceptance criteria; change-control log; reviewable approval citation (URL and approved scope revision); current status; evidence links.

## Boundary rules
1. The owner approves a specific umbrella scope revision. Approval is NOT inferred from creation, labels, checklist, milestone assignment, or JSON values.
2. Child issues must be within the approved umbrella scope, explicitly associated with that umbrella, and independently approved for execution.
3. PRs must reference one approved child (and parent umbrella). No PR may use the umbrella to justify unrelated changes.
4. If scope, acceptance, exclusions or child membership changes, pause affected execution until explicit human reapproval. Do not expand scope by convenience.
5. A child may close only with linked PR/evidence and acceptance review; a parent umbrella closes only when its own acceptance is approved and its children reconciled.
6. Report blockers/ambiguous rules, do not assume approvals or generate fictitious completion metrics.
7. Wiki reports are snapshots of observed Issue/PR/CI states; unverified values are `unknown` or `not_collected`, never zero.

## State model
`draft → pending_approval → approved → active → review → accepted → closed`; `blocked` and `change_requested` are interrupt states. This is a documentation convention, not an automatic GitHub workflow.

## Proposed vs actual
Milestones M01–M07 are **proposed mapping IDs** only. Actual GitHub Issue/PR numbers, authorizations, assignees, due dates, tests and status remain unknown until read from GitHub and verified.

## v0.0.7 portability / label / complaint addendum
GitHub-specific wording in historical workflow text means **the verified active provider (GitHub or GitLab)**. Work IDs remain canonical; actual URLs/IDs are stored only in `rag/provider_bindings.json` after verification. The native PR is a GitLab MR when GitLab is active. Labels classify but do not grant Human approval. Internal operational complaints are recorded in `COMPLAIN.md`; escalation requires separate authorization. Evidence-based Wiki reports remain unpublished staging until authorized.
