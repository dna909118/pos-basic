# COMPLAIN — BYAR BARBER Engineering Operations

**Register state:** ACTIVE DOCUMENT / EMPTY REGISTER. **Recorded complaints:** 0 (local entries). This does **not** claim there are no real incidents; none have been reported and entered here yet.

This file records **engineering operations complaints**, not BYAR BARBER product feature requests. It covers coding agent scope deviations, governance violations, RAG index/retrieval issues, CI/CD blockers, provider portability, source/document contradictions, and incorrect Wiki evidence.

## Mandatory record attributes

Each recorded complaint must have an immutable local ID (`OEC-001` onward), detection date (with time zone if known), reporter/source, category, severity, status, related canonical work IDs, expected/actual behavior, evidence (or `not_collected`), impact, investigation, decision, resolution, history, and optional verified GitHub/GitLab escalation links.

Allowed status lifecycle: `open` → `triaged` → `investigating` → `resolved` → `closed`. `blocked` or `reopened` may be used with explicit evidence; these are complaint states, not Issue approval states. Severity values: `critical`, `high`, `medium`, `low`, or `untriaged`.

**Rules:**
- A complaint is a record of an observation, **not** permission to modify code, create platform Issues, publish Wiki, or close an approved task.
- Human triage is required before escalation. Any follow-up change must use an authorized Umbrella/Child Issue or a direct bounded human instruction.
- Preserve prior investigation and decision history; redact secrets and sensitive personal information from public repository snapshots.
- Update `rag/complaints.json` consistently. Evidence and provider references must be real; `null` / `not_collected` when absent.
- Wiki reporting draws only from verified records and clearly distinguishes registered counts from actual provider incidents.

## Recorded complaints

_No complaints registered in the current bundle._

## Recording format

Copy `management/complaint_entry_template.md` and append a completed record here **only when an actual complaint is raised**. Do not publish sample complaints as real incidents.
