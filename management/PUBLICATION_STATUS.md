# Governance publication status

Repository: https://github.com/dna909118/pos-basic

Publication was authorized directly by the Human request to continue steps 5 and 6. This authorizes object publication only, not scope acceptance, worker execution, model inference, Wiki publication, or merge of this registry update.

## Verified publication

- 35 canonical labels published; 10 existing repository labels preserved (45 total).
- 7 open Milestones, 7 open Umbrella Issues and 40 open Child Issues verified by live API reads.
- Labels, canonical ID prefixes, milestone assignments and Child-to-Umbrella body links verified.
- 54 verified GitHub bindings recorded; 7 planning-only PR bindings remain not_created.
- All 47 execution approval records remain pending_approval; approval evidence fields remain null.
- GitLab references remain null; source draft text, draft hashes and product documents are unchanged.
- Issue bodies contain unchanged draft snapshots plus a publication-state header and exact scope hash. Original null/not-created placeholders describe the source snapshot, not the current provider state.
- Provider export files and work_drafts remain source drafts; provider_bindings is the authoritative local registry for verified native references.

## Repository settings blocked

- Default branch is still chore/byar-barber-v008-bootstrap. PATCH to set main returned HTTP 403: Resource not accessible by integration.
- Branch-protection GET/PUT returned HTTP 403: Resource not accessible by integration. No successful protection update is claimed.
- Ruleset API reports: Upgrade to GitHub Pro or make this repository public to enable this feature. Repository visibility remains private.
- Owner action: set default branch to main under GitHub Settings; enable available protection after resolving account-plan and integration-permission prerequisites. Preserve private visibility unless explicitly authorized otherwise.
- Suggested protection: require PR review (one independent approval), require validate, dismiss stale approvals, resolve conversations, prevent force pushes/deletion. flutter-web is path-filtered; do not require it globally unless its workflow is changed to report for every PR.

## Validation and source provenance

Live inventory verification PASS. Governance validator and all 40 offline tests PASS; FTS5 ready, canonical lookup and payment search PASS.
The no-local-approval test now checks pending approval and null evidence for each Umbrella/Child rather than equating publication with approval.
RELEASE_SHA256.txt remains the original v0.0.8-r1 archive manifest. verify_release.py intentionally reports mismatches for AGENTS.md, rag/provider_bindings.json and tests/test_bootstrap.py after this authorized publication update. The manifest was not rewritten to conceal these changes; review them against the original release commit 1ae56c42b68a8a35debe407ff2db485cee3ffde8. All other manifest entries matched.

## Canonical provider map

| Canonical ID | Kind | Verified GitHub URL |
| --- | --- | --- |
| M01 | milestone | https://github.com/dna909118/pos-basic/milestone/1 |
| M02 | milestone | https://github.com/dna909118/pos-basic/milestone/2 |
| M03 | milestone | https://github.com/dna909118/pos-basic/milestone/3 |
| M04 | milestone | https://github.com/dna909118/pos-basic/milestone/4 |
| M05 | milestone | https://github.com/dna909118/pos-basic/milestone/5 |
| M06 | milestone | https://github.com/dna909118/pos-basic/milestone/6 |
| M07 | milestone | https://github.com/dna909118/pos-basic/milestone/7 |
| UMB-M01 | umbrella | https://github.com/dna909118/pos-basic/issues/2 |
| UMB-M02 | umbrella | https://github.com/dna909118/pos-basic/issues/3 |
| UMB-M03 | umbrella | https://github.com/dna909118/pos-basic/issues/4 |
| UMB-M04 | umbrella | https://github.com/dna909118/pos-basic/issues/5 |
| UMB-M05 | umbrella | https://github.com/dna909118/pos-basic/issues/6 |
| UMB-M06 | umbrella | https://github.com/dna909118/pos-basic/issues/7 |
| UMB-M07 | umbrella | https://github.com/dna909118/pos-basic/issues/8 |
| CI-01 | child | https://github.com/dna909118/pos-basic/issues/9 |
| CI-02 | child | https://github.com/dna909118/pos-basic/issues/10 |
| CI-03 | child | https://github.com/dna909118/pos-basic/issues/11 |
| CI-04 | child | https://github.com/dna909118/pos-basic/issues/12 |
| CI-05 | child | https://github.com/dna909118/pos-basic/issues/13 |
| CI-06 | child | https://github.com/dna909118/pos-basic/issues/14 |
| CI-07 | child | https://github.com/dna909118/pos-basic/issues/15 |
| CI-08 | child | https://github.com/dna909118/pos-basic/issues/16 |
| CI-09 | child | https://github.com/dna909118/pos-basic/issues/17 |
| CI-10 | child | https://github.com/dna909118/pos-basic/issues/18 |
| CI-11 | child | https://github.com/dna909118/pos-basic/issues/19 |
| CI-12 | child | https://github.com/dna909118/pos-basic/issues/20 |
| CI-13 | child | https://github.com/dna909118/pos-basic/issues/21 |
| CI-14 | child | https://github.com/dna909118/pos-basic/issues/22 |
| CI-15 | child | https://github.com/dna909118/pos-basic/issues/23 |
| CI-16 | child | https://github.com/dna909118/pos-basic/issues/24 |
| CI-17 | child | https://github.com/dna909118/pos-basic/issues/25 |
| CI-18 | child | https://github.com/dna909118/pos-basic/issues/26 |
| CI-19 | child | https://github.com/dna909118/pos-basic/issues/27 |
| CI-20 | child | https://github.com/dna909118/pos-basic/issues/28 |
| CI-21 | child | https://github.com/dna909118/pos-basic/issues/29 |
| CI-22 | child | https://github.com/dna909118/pos-basic/issues/30 |
| CI-23 | child | https://github.com/dna909118/pos-basic/issues/31 |
| CI-24 | child | https://github.com/dna909118/pos-basic/issues/32 |
| CI-25 | child | https://github.com/dna909118/pos-basic/issues/33 |
| CI-26 | child | https://github.com/dna909118/pos-basic/issues/34 |
| CI-27 | child | https://github.com/dna909118/pos-basic/issues/35 |
| CI-28 | child | https://github.com/dna909118/pos-basic/issues/36 |
| CI-29 | child | https://github.com/dna909118/pos-basic/issues/37 |
| CI-30 | child | https://github.com/dna909118/pos-basic/issues/38 |
| CI-31 | child | https://github.com/dna909118/pos-basic/issues/39 |
| CI-32 | child | https://github.com/dna909118/pos-basic/issues/40 |
| CI-33 | child | https://github.com/dna909118/pos-basic/issues/41 |
| CI-34 | child | https://github.com/dna909118/pos-basic/issues/42 |
| CI-35 | child | https://github.com/dna909118/pos-basic/issues/43 |
| CI-36 | child | https://github.com/dna909118/pos-basic/issues/44 |
| CI-F01 | child | https://github.com/dna909118/pos-basic/issues/45 |
| CI-F02 | child | https://github.com/dna909118/pos-basic/issues/46 |
| CI-R01 | child | https://github.com/dna909118/pos-basic/issues/47 |
| CI-R02 | child | https://github.com/dna909118/pos-basic/issues/48 |
