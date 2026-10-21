# Clean Bundle and Repository Change Control

v0.0.7 is immutable historical input. v0.0.8 is a candidate clean bootstrap artifact. GitHub/GitLab provider IDs recorded in historical repositories must never be copied into a new repository; all bootstrap bindings are null. Source specifications, canonical work IDs, and labels are retained unless Human approves a specific change.

For subsequent changes after first accepted repository commit:

1. Human submits a bounded change request: exact file, current baseline, desired difference and scope.
2. Start from accepted `main`, never unzip an old bundle over a populated repository.
3. Inspect impact on TSD → Storyboard → Lo-Fi → JSON mapping, work issue scope, and active PR dependencies.
4. Modify only the approved files in a dedicated branch; run offline validators and relevant tests.
5. Present diff, CI evidence and dependency/approval impact for Human review before merge.
6. Once merged, Git becomes the current accepted source baseline; GitHub live Issue approvals remain independent.
7. Rebuild SQLite FTS5 after changes to indexed sources. Reapprove Umbrella/Child scopes if canonical approved bytes change.
8. Export a new tagged bundle **only when a versioned release is needed**; always preserve historical archive.

A clean repo reset is a separate destructive operation, not authorized by this v0.0.8 bundle creation. GitHub Projects, Wiki, labels, Milestones, Issues and environment publication are not performed by unzipping a bundle.
