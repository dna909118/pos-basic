# GitHub Free Private — Soft Governance Contract (BYAR BARBER)

**Target repository:** `dna909118/pos-basic` (intent/configuration, not proof of current live provider state).  
**Provider:** GitHub Free · **Visibility:** Private · **Mode:** `soft_governance`.  
**Portability:** GitLab remains a target, not a simultaneously active governance source.

## Platform limits

GitHub Free on private repositories does **not** provide enforceable branch protection/rulesets for the required review/status-check policies. Therefore the following are NOT enforceable by native branch settings:

- Prevent direct push to `main` by authorized write users.
- Require PR review approval before merge.
- Require successful CI/status checks before merge.
- Prevent a write-authorized Human from bypassing review and CI.

Do **not** label the repository `protected`, `branch-rules enforced`, or `merge-blocked by CI`. CI PASS is evidence only, not an enforced merger condition. Upgrading the account or making the repository public is **not** part of this bundle.

Reference: GitHub documentation for branch rules and rulesets (verify with GitHub on any future plan change):
- https://docs.github.com/en/rest/branches/branch-protection
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets

## Compensating controls (procedural, NOT hard enforcement)

1. Human approves publication of native governance objects; scope execution approvals for Umbrella and Child are independent.
2. On agent dispatch, live provider preflight verifies active repository, binding, approved scope revision and SHA-256, approver allowlist, and dependencies. Approval labels alone do not suffice.
3. GitHub Actions agent job has `contents: read`, excludes Human-only design assets, and emits artifact-only patches/evidence; it has no repository write, PR creation or merge authority.
4. Engineers conventionally use branch → PR → CI → Human review → explicit Human merge. A privileged user **can bypass this convention** because Free/private lacks native rules. Human must examine CI status before accepting a PR.
5. Staged Wiki reports must label merge-policy compliance as `not_platform_enforced` and must not claim a merge was blocked by GitHub protection.
6. A non-agent publisher introduced in future needs separate authorization and minimum-scoped credentials; no automatic publisher is delivered.

## Operative policy and validator

Source of intended mode: `management/providers/github_free_private_policy.json`. Offline validator rejects inconsistent plan/mode, unsupported native-enforcement claims and privilege escalation in the packaged manual agent workflow. Preflight additionally checks `GITHUB_REPOSITORY` against the configured target. The validator **does not** prove remote repository settings, actual branch permissions, live approval validity or Human compliance; these require independent verification.

No repository reset, visibility change, account upgrade or native publication is authorized by this document.
