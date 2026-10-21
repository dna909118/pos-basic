# BYAR BARBER v0.0.8 — Clean Engineering Bootstrap Bundle

- Base archive: BYAR_BARBER_v0.0.7.zip (source retained; prior ZIP untouched).
- Product TSD, Storyboard, Lo-Fi, Design System, and Human-only Hi-Fi asset preserved **byte-for-byte**.
- 7 milestones, 7 umbrellas, 40 children, 7 PR plans, 35 label definitions, 47 assignments, and 61 provider bindings retained as canonical drafts.
- Active provider selected: GitHub, portability target: GitLab. Repository identity is unconfigured, native IDs/URLs remain null, no approval claimed.
- Active retrieval: offline SQLite FTS5; legacy Chroma runtime removed from active bundle. No embeddings/model files/downloads.
- Adds headless OpenCode V2 and mini-SWE-agent V2 adapters, deterministic task/result contracts, fail-closed online provider preflight, manual GitHub Actions artifact-only dispatch, and JSON/offline tests.
- MCP documented as an integration contract only; Hermes excluded. Obsidian/Jelastic/Windmill are not mandatory.
- No Flutter implementation and no user repository mutation performed. CI execution against GitHub and live model-agent integration require external credentials and must be reported separately.
- Run tests and review `RELEASE_VALIDATION.md` before adopting. SHA256 manifest is `RELEASE_SHA256.txt`.

## v0.0.8-r1 — Flutter builder configuration completion
This non-destructive release revision adds the Flutter 3.44.0/Dart 3.12.0 stable web-builder contract, pinned Mix 2.2.2, `tools/flutter_builder.py`, dry-run/offline tests and GitHub Actions `flutter-builder.yml`. It supports ephemeral smoke compilation independent of business application source and building a future approved `app/` with committed lockfile. No Flutter feature implementation is included. The historical v0.0.8 ZIP remains intact.

## v0.0.8-r2 — GitHub Free private policy
Non-destructive configuration refinement: set `dna909118/pos-basic` as intended provider target, retain GitHub Free/private and GitLab portability. Add machine-readable `soft_governance` policy, explanatory contract and offline enforcement-consistency tests. CI and Human PR review remain procedural: no platform-enforced branch rules, required checks or merge-review gates. Existing manual artifact-only dispatch and Flutter builder stay intact. No live provider settings, Issue, PR or source specifications were modified.
