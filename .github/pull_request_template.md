> **Governance:** Reference approved Umbrella Issue (URL + revision), authorized Child Issue (URL + approval), and Milestone. Without those approvals do not merge.

- Umbrella / revision:
- Child Issue / approval evidence:
- Milestone:
- CI run and test evidence:
- Scope deviations (if any, STOP and reapprove):

# BYAR BARBER — Pull Request

## Linked approved issue
Issue: #<!-- number -->
Approval reference (comment/link): <!-- proof of human authorization -->

## Approved scope and implementation
- Changes within issue:
- Files changed:
- Out-of-scope changes: None / describe and request approval

## Source traceability
- TSD §:
- Storyboard SB-:
- Lo-Fi SC-:
- RAG trace IDs:

## Verification evidence
- [ ] `flutter pub get` (result/link)
- [ ] `dart format --output=none --set-exit-if-changed .` (result/link)
- [ ] `flutter analyze` (result/link)
- [ ] `flutter test` (result/link)
- [ ] `flutter build web --release` (result/link)
- [ ] Browser/PWA checks (result/limitation)
- [ ] RAG JSON index checked for relevant traceability changes

## Human review
- [ ] Reviewer approved
- [ ] No auto-merge

## Known limitations

## Portable governance metadata
- Canonical work IDs (do not replace with provider numbers):
- Proposed/observed labels from `rag/label_assignments.json`:
- Provider binding evidence (only actual URLs):
- Operations complaint ID (`OEC-*`) if related, or N/A:

GitLab equivalent: `.gitlab/merge_request_templates/Engineering_Change.md`. Labels never grant approval.
