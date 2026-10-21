# BYAR BARBER v0.0.8 — Validation and Known Limits

## Source baseline and fidelity

- Source: verified complete `/mnt/data/BYAR_BARBER_v0.0.7.zip`, 123 file entries; incomplete prior loose-folder copy not used.
- Product TSD, UX Storyboard, Lo-Fi, Design System, and Human-only Hi-Fi image compared byte-for-byte against v0.0.7 and **all five matched**. The Human-only image is included for Human review only; agent access/indexing is prohibited.
- Canonical work inventory preserved: 7 Milestones, 7 Umbrellas, 40 Child Issues, 7 PR drafts, 35 labels, 47 proposed Issue-label assignments, 61 provider bindings.
- Clean bootstrap: active provider GitHub; GitLab portability target; **all 61 published objects remain not_created and all provider native references null**. No previous PR/Issue number, execution permission or live Wiki data is imported.

## Tests executed locally (offline, Python 3 standard library)

| Gate | Result |
|---|---|
| `python tools/validate_governance.py` | PASS |
| `python -m unittest discover -s tests -v` | PASS — 29 tests |
| `python rag/fts5/operational_index.py build` | PASS |
| `python rag/fts5/operational_index.py status` | PASS — ready true |
| `python rag/fts5/operational_index.py lookup REF-SB-16` | PASS |
| `python rag/fts5/operational_index.py query "pembayaran DP pelunasan" --top-k 3` | PASS |
| Manual source hash comparison vs original v0.0.7 ZIP | PASS — 5 protected original files identical |
| Smoke/dry-run invocation of both worker adapters using synthetic manifests | PASS — no external model invoked |

The current source index contained **101 indexed files / 405 chunks** on an earlier build; counts may change as source documents change. The authoritative count is the latest `status` command run on the exact extracted release.

## NOT verified — external execution / Human gates

- No live GitHub Actions run of the new v0.0.8 workflows has been performed.
- No API provider/model inference is configured; actual OpenCode V2 and mini-SWE-agent V2 CLI execution, latency, cost and model quality are unverified.
- No GitLab CI execution / native GitLab provider adapter is delivered. GitLab portability is canonical-data and documentation compatibility only.
- No automated PR publisher, autonomous queue, duplicate-proof persistent scheduler, or merge authority is delivered. Agent workflow is manual and artifact-only.
- No production-grade hard isolation of inference credentials against malicious code running in a worker has been demonstrated.
- MCP is documented as an optional protocol contract; a running MCP server does not exist.
- No GitHub labels, Milestones, Issues, Projects, Wiki pages, branches or secrets have been published from this bundle task.
- No Flutter feature application code from historical PR #5/#6 is imported automatically.

## Remaining operator-controlled initialization

See `orchestration/README.md` for approved issue publication, scope approval comment syntax, allowlisted Human identities, model secrets, GH Actions dispatch and evidence-based review. Every live operation requires separate Human authorization. This bundle remains a **release candidate pending external smoke tests and Human acceptance**, not an operationally active agent platform.

## v0.0.8-r1 — Flutter builder validation boundary
The builder contract, CLI and workflow have been added for GitHub Actions; offline unit tests and config checks verify structure and expected failure modes. This environment does **not** have Flutter/Dart installed, so actual Flutter/Mix resolution, analyzer, tests, web build, and Actions artifact upload remain **NOT VERIFIED** until the CI workflow is run. Source integrity and other v0.0.8 checks must be rerun against this revision.

### v0.0.8-r1 actual local verification
- `python tools/flutter_builder.py config`: PASS (offline builder configuration).
- `python -m unittest discover -s tests -v`: PASS — **40 tests** (29 prior + 11 builder tests).
- `python tools/validate_governance.py`: PASS (draft structure, no live publication claims).
- Flutter 3.44.0 / Dart 3.12.0 / Mix 2.2.2 are pins **configured** in bundle, not installed or compiled locally.
- `subosito/flutter-action@v2` and artifact upload must be tested after import in GitHub Actions; no live Flutter CI was executed here.
- Protected five source files, including Human-only Hi-Fi, remained byte-identical to the original v0.0.8 baseline.

### v0.0.8-r1 actual local verification
- `python tools/flutter_builder.py config`: PASS (offline builder configuration).
- `python -m unittest discover -s tests -v`: PASS — **39 tests** (29 prior + 10 builder tests).
- `python tools/validate_governance.py`: PASS (draft structure, no live publication claims).
- Flutter 3.44.0 / Dart 3.12.0 / Mix 2.2.2 are pins **configured** in bundle, not installed or compiled locally.
- `subosito/flutter-action@v2` and artifact upload must be tested after import in GitHub Actions; no live Flutter CI was executed here.
- Protected five source files, including Human-only Hi-Fi, remained byte-identical to the original v0.0.8 baseline.

## v0.0.8-r2 — GitHub Free Private soft governance (latest authoritative check)

- Active target configuration: `dna909118/pos-basic` (expected repository identity, **not** evidence of actual live GitHub settings).
- GitHub remains Free/private. `soft_governance` is the declared mode, not hard branch protection. Native branch rules/rulesets, required PR reviews/status checks and protection against direct pushes are **not available/enforced** at this tier. CI and Human review are procedural requirements; GitHub itself cannot be claimed to block an authorized write-user from bypassing them.
- GitLab remains the portability target. No automatic merger, publisher, repository write permission for workers, or plan upgrade is authorized.
- Added `management/providers/github_free_private_policy.json` and `GITHUB_FREE_PRIVATE_GOVERNANCE.md`, repository match preflight, policy-aware governance validator and negative tests for contradictory hard-enforcement claims/write permissions.
- Actual offline validation on this revision: `python tools/validate_governance.py` **PASS**; `python -m unittest discover -s tests -q` **PASS — 49 tests**; `python tools/bootstrap_check.py` **PASS**; `python tools/flutter_builder.py config` **PASS**; SQLite FTS5 `ready: true`, **104 indexed sources / 414 chunks**, canonical lookup and payment query **PASS**. Counts are derived snapshots and may change after documentation updates.
- Five protected source assets (TSD, Storyboard, Lo-Fi, Design System and Human-only Hi-Fi) are byte-identical to source v0.0.8-r1. Human-only Hi-Fi was not opened or used for agent context.
- Flutter SDK and live GitHub Actions compilation, agent inference, provider permission verification and runtime native branch enforcement remain **NOT VERIFIED** by this offline bundle. GitHub account/repository settings were not modified.
- The above is the **current** r2 validation; historical r1 entries in this document describe previous checkpoints, not current test counts.
