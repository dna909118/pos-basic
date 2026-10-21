# CI-F01 — Verifikasi environment Flutter/Dart & dependensi

**Child:** `CI-F01` · **Umbrella:** `UMB-M01` · **Milestone:** `M01`
**Type:** engineering prerequisite (bukan fitur TSD tambahan)
**Approved scope revision:** `draft-1`
**Child scope sha256:** `0397e7c5321904cd90f449b55c3ca45e690c51d8d7a0c47b24883d9c33caa27b`
**Umbrella scope sha256:** `6aca36c8b7b05ac32e8cea924b9741186fe5399326dbf7c65b42bd008de51d8d`

This report records the *actually executed* audit of the Flutter project, the
execution environment, and the Mix dependency before implementation. It does not
add product requirements or business features, and it does not modify provider
state, approvals, Issues, or PRs.

## Scope (as approved)

> Audit project Flutter, environment Codex Cloud, dan dependency Mix sebelum implementasi.

Boundary: changes are limited to this verification scope. No `app/` business
implementation, TSD/Storyboard/Lo-Fi/Design System, provider state, approvals,
Issue status, or merge was changed. No Human-only Hi-Fi (`design/`) was accessed.

## Verification environment

| Item | Pinned contract (`builder/flutter/toolchain.json`) | Observed | Result |
| --- | --- | --- | --- |
| Flutter | 3.44.0 (stable) | 3.44.0 (stable) | PASS |
| Dart | 3.12.0 | 3.12.0 | PASS |
| Target platform | web | web | PASS |
| Mix | 2.2.2 | 2.2.2 (resolved, `sha256:15b70de5…52548`) | PASS |

These commands ran on the GitHub Actions worker for `dna909118/pos-basic`,
not on the interactive Codex cloud machine. The SDK observations below establish
readiness of that GitHub-hosted runner only. Flutter/Dart installation and
execution in the interactive Codex cloud machine were not verified by this pilot.

Evidence run: https://github.com/dna909118/pos-basic/actions/runs/39652677798

Source commit: `f56b19d9ebed56c8332fc97520d1aeac57a11871`.
The run's preflight verified the live independent approvals and exact scope hashes.
This report was reviewed against the uploaded trajectory and worker logs; the
original artifact remains unchanged.

## Dependency audit

- `mix: 2.2.2` resolves on Dart 3.12.0 / Flutter 3.44.0.
- Transitive `mix_annotations 2.2.0` resolved successfully.
- `pub get` completed: "Changed 2 dependencies!".
- No dependency constraint conflict between the pinned SDK and Mix 2.2.2.

## Executed commands and results

| # | Command | Result |
| --- | --- | --- |
| 1 | `python tools/flutter_builder.py config` | PASS — config valid |
| 2 | `python tools/flutter_builder.py doctor` | PASS — Flutter 3.44.0 / Dart 3.12.0 match |
| 3 | `flutter pub get` (mix 2.2.2 fixture) | PASS — mix 2.2.2 + mix_annotations 2.2.0 |
| 4 | `flutter analyze --no-pub` | PASS — "No issues found!" |
| 5 | `flutter test --no-pub` | PASS — 1 test passed |
| 6 | `flutter build web --release --no-pub --base-href /` | PASS — "Built build/web" |
| 7 | `python tools/flutter_builder.py smoke --artifact-dir <tmp>` | PASS — `index_html: true` |
| 8 | `python -m unittest discover -s tests -v` | PASS — 49 tests OK |

The canonical builder smoke output:

```json
{
  "status": "PASS",
  "mode": "smoke",
  "flutter": "3.44.0",
  "mix": "2.2.2",
  "artifact_dir": "<tmp>/byar-flutter-smoke",
  "index_html": true
}
```

## Module status

- Flutter/Dart toolchain — **Complete** (verified).
- Mix dependency (2.2.2) — **Complete** (resolved, analyzed, built).
- Web target build — **Complete** (release build + smoke artifact produced).
- Flutter business application under `app/` — **Not started** (out of scope; no
  authorized application exists and none was created).
- GitHub Actions pilot runner — **Verified** — preflight, runtime check, worker
  execution and review-artifact upload succeeded in run 39652677798. The pilot
  invoked the Flutter builder directly; it did not dispatch the separate
  `flutter-builder.yml` workflow.
- Interactive Codex cloud SDK — **Not verified by this pilot**.

## Blockers / owner-required steps

- Flutter/Dart availability in the interactive Codex cloud machine still requires
  a separate check if that machine must run Flutter. The pilot verifies the
  GitHub Actions execution environment, not every development environment.
- Successful runner execution is not Human acceptance or Issue closure.
- No `app/` target exists; a real product build requires the separately
  approved application Child Issue and a committed `pubspec.lock`.

## Evidence limits and review

The trajectory shows `exit_status: Submitted`, 30 recorded model calls and an
estimated model cost of USD 0.009595056. That is agent-side accounting, not a
verified provider invoice. The wrapper records `tests: not_collected`; the test
results above were verified from the trajectory's command outputs instead.

Some ad-hoc commands piped output through `tail` or ran builds in the background,
so their shell exit codes alone are insufficient evidence. The later canonical
builder smoke emitted `status: PASS` and `index_html: true`, and its captured
output contains the successful analyzer, one Flutter test and release build.
The unittest outputs explicitly show `Ran 49 tests` and `OK`; governance output
reports `PASS`. These are historical results from this runner, not new local
runs performed during artifact review.

The reviewed patch excludes `dispatch-input/dispatch.json`: it is an ephemeral
runner input, not an implementation change. The original artifact is preserved.
No Flutter business application is included, implemented or verified.

## Boundary statement

The pilot worker kept changes local for patch review and performed no push, PR,
merge, Issue closure or Wiki publication. This reviewed report is subsequently
submitted through a separate documentation PR. Human acceptance of CI-F01 and
any merge or Issue closure remain separate provider actions.
