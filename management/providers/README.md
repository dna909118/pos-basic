# Provider adapter drafts — no remote mutation

- `github_labels.draft.json` — GitHub label creation payload candidates (`name`, `color`, `description`).
- `gitlab_labels.draft.json` — GitLab label creation payload candidates (`name`, `color` with `#`, `description`).
- `rag/provider_bindings.json` — canonical local-to-provider identity map; every native reference is initially null.
- `.github/ISSUE_TEMPLATE/` + `.github/pull_request_template.md` — GitHub forms/templates.
- `.gitlab/issue_templates/` + `.gitlab/merge_request_templates/` — GitLab Markdown description templates.

These files are **offline drafts**. They neither create actual remote objects nor assert that a particular provider supports every feature/approval rule. Manual publishing and review remain human-controlled.

## GitHub Free private target (v0.0.8-r2)
Use `github_free_private_policy.json` and `GITHUB_FREE_PRIVATE_GOVERNANCE.md`. No GitHub Free private branch/ruleset enforcement is assumed. Target: `dna909118/pos-basic`. No provider objects are published by unpacking this bundle.
