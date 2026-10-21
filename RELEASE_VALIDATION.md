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
