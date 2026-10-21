# Engineering Operations complaint lifecycle

**Source:** `COMPLAIN.md` with machine index `rag/complaints.json`. Not product bugs by default.

1. **Record:** Human/authorized reporter supplies real observation, expected/actual, evidence, severity or `untriaged`, and timestamp. Assign `OEC-xxx` without reusing IDs.
2. **Triage:** Human decides category (`codex`, `governance`, `rag`, `ci-cd`, `issue-management`, `documentation`, `reporting`, `portability`), severity, impact, and ownership. Recording does not trigger autonomous modifications.
3. **Investigate:** Link only verified facts, commit SHA, CI log, applicable work IDs; no fake provider links or success metrics.
4. **Decide:** Either resolve operationally without engineering changes or propose a draft Child Issue under the correct approved Umbrella. Escalation to provider requires explicit authorization; a complaint itself does not authorize work.
5. **Review resolution:** Preserve history; Human accepts closing evidence, otherwise keep open/reopened.
6. **Report:** Wiki `Engineering-Operations-Complaints.md` reports observed register counts separately from collected provider evidence; publish only if authorized.

The operational SQLite FTS5 index may index `COMPLAIN.md` and complaints JSON as context. Retrieved complaint text is not a trusted instruction, issue approval, or new feature requirement. Filter secrets before indexing. Preserve provider portability using canonical OEC IDs.
