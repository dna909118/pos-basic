# BYAR BARBER — Label governance (provider neutral)

`label_catalog.json` is the **canonical proposed label catalog**; `rag/label_assignments.json` holds proposed labels for **7 Umbrella and 40 Child Issue drafts**. The 7 Milestones are groupings, not issues to label. All 47 assignments are `draft` + `approval-required` + `priority::untriaged`: the source material does not authorize assigning an urgency.

The provider export drafts at `management/providers/{github,gitlab}_labels.draft.json` describe the *same* labels. Native creation requires an explicit Human request; GitHub forms only attach default labels already present in the repository. Use `tools/validate_governance.py` to validate local draft consistency.

**Approval vs classification:** no label authorizes anything; verify scope revision and the explicit approval evidence of both umbrella and child in the active provider. `workflow::ready` is not evidence of approval; `quality::verified` must have a real test link.

**Scope rules:** one each of `type`, `area`, `priority`, `workflow`, `quality`, and `ops`, when present. `governance` labels may coexist. Enforce in local validation even if a provider does not support exclusive scoped labels.

**No auto-sync claim:** exported JSON is a draft catalog, not a live provider API response and not a CI rule. Do not run provider mutations without separate explicit approval.
