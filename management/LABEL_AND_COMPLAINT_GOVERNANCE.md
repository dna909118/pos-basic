# Classification, portability and engineering operations governance

The **label catalog** is a classification tool, not a safety or authorization gate by itself. Draft assignments for 40 Child Issues and 7 Umbrellas already exist, so this is implementation-ready staging rather than empty templates. Human-controlled urgency is explicitly `priority::untriaged` until triage. GitHub/GitLab native labels are not created in this bundle.

For approved execution: verify provider object exists, approved parent scope revision, membership, independently approved Child Issue, human evidence URL, permitted files/actions, branch/review constraints; label state cannot replace any of these checks. The current bundle **does not yet implement provider API authorization checks**; fail closed when actual approval evidence cannot be verified.

An engineering operations complaint in `COMPLAIN.md` may point to a proposed escalation; it must never trigger creating an Issue, a PR/MR, source changes, or runtime actions without additional explicit Human authorization. Track complaints via canonical `OEC-xxx` IDs, report to Wiki from evidence, and preserve human-only Hi-Fi exclusion.

Provider binding remains nullable until actual objects exist. See `management/PORTABILITY_CONTRACT.md` and `management/COMPLAINT_LIFECYCLE.md`.
