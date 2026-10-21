#!/usr/bin/env python3
"""Offline structural validator for canonical BYAR BARBER governance drafts.

This validates local consistency; it DOES NOT verify provider permission/approval,
actual CI, Wiki publication or SQLite FTS5 runtime.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))

def validate():
    problems = []
    def check(condition, message):
        if not condition:
            problems.append(message)

    catalog = load("management/labels/label_catalog.json")
    assignments = load("rag/label_assignments.json")
    work = load("rag/work_drafts.json")
    providers = load("rag/provider_bindings.json")
    complaints = load("rag/complaints.json")
    wiki = load("rag/wiki_reporting.json")
    cset = {l["name"] for l in catalog["labels"]}
    check(len(cset) == len(catalog["labels"]), "Duplicate canonical labels")
    check(all(re.fullmatch(r"[a-z0-9-]+::[a-z0-9-]+", l) for l in cset), "Malformed scoped label")
    check(all(re.fullmatch(r"[A-F0-9]{6}", l["color"]) for l in catalog["labels"]), "Invalid color token")

    milestones = {x["draft_id"]: x for x in work["milestones"]}
    umbrellas = {x["draft_id"]: x for x in work["umbrellas"]}
    children = {x["draft_id"]: x for x in work["child_issues"]}
    plans = {x["draft_id"]: x for x in work["pr_plans"]}
    expected = {**umbrellas, **children}
    amap = {x["work_id"]: x for x in assignments["assignments"]}
    check((len(milestones), len(umbrellas), len(children), len(plans)) == (7, 7, 40, 7), "Unexpected draft cardinality")
    check(set(amap) == set(expected), "Assignments missing/orphaned for draft work")
    check(len(amap) == len(assignments["assignments"]), "Duplicate label assignment ID")

    for mid, m in milestones.items():
        check(m["umbrella_id"] in umbrellas, f"{mid}: missing umbrella")
    child_ids_by_parent = Counter()
    for cid, c in children.items():
        uid = c["umbrella_id"]
        child_ids_by_parent[uid] += 1
        check(uid in umbrellas, f"{cid}: no valid umbrella")
        check(c["milestone_id"] in milestones, f"{cid}: no valid milestone")
        if uid in umbrellas:
            check(c["milestone_id"] == umbrellas[uid]["milestone_id"], f"{cid}: parent/milestone mismatch")
            check(cid in umbrellas[uid]["child_draft_ids"], f"{cid}: not in parent's child register")
    for uid, u in umbrellas.items():
        check(set(u["child_draft_ids"]) == {cid for cid, c in children.items() if c["umbrella_id"] == uid}, f"{uid}: child register mismatch")
        check(u["milestone_id"] in milestones, f"{uid}: missing milestone")

    for wid, w in expected.items():
        labels = w["labels"]
        check(wid in amap and amap[wid]["labels"] == labels, f"{wid}: divergent assignment")
        check(all(l in cset for l in labels), f"{wid}: undefined proposed label")
        check("workflow::draft" in labels and "priority::untriaged" in labels and "governance::approval-required" in labels, f"{wid}: draft guards missing")
        scopes = [l.split("::", 1)[0] for l in labels]
        for scope in catalog["policy"]["exclusive_scopes"]:
            check(scopes.count(scope) <= 1, f"{wid}: duplicate exclusive scope {scope}")
        if wid in umbrellas:
            check("type::umbrella" in labels, f"{wid}: missing umbrella type")
            file = ROOT / "management" / "drafts" / "umbrellas" / f"{wid}.md"
        else:
            check("type::task" in labels, f"{wid}: missing child type")
            files = list((ROOT / "management" / "drafts" / "issues").glob(f"{wid}_*.md")) + list((ROOT / "management" / "drafts" / "issues").glob(f"{wid}.md"))
            check(len(files) == 1, f"{wid}: wrong number of draft files")
            file = files[0] if files else None
        if file is not None:
            check(file.is_file(), f"{wid}: missing draft file")
            if file.is_file():
                content = file.read_text(encoding="utf-8")
                check("## Platform-neutral proposed labels (DRAFT)" in content, f"{wid}: missing label block")
                check(all(f"`{label}`" in content for label in labels), f"{wid}: label block out of sync")

    binding_ids = [b["local_id"] for b in providers["bindings"]]
    check(len(binding_ids) == len(set(binding_ids)) == 61, "Provider bindings must contain 61 unique local IDs")
    check(set(binding_ids) == set(milestones) | set(umbrellas) | set(children) | set(plans), "Provider binding ID mismatch")
    check(providers["active_provider"] == "github" and providers["portability_target"] == "gitlab", "Invalid provider selection")
    for b in providers["bindings"]:
        state = b.get("status")
        check(state in {"not_created", "published"}, f"{b['local_id']}: invalid status")
        active = providers["active_provider"]
        for forge, nativeid in [("github", "number"), ("gitlab", "iid")]:
            vals = b[forge]
            complete = all(vals.get(k) is not None for k in ["url", nativeid, "verified_at"])
            empty = all(vals.get(k) is None for k in ["url", nativeid, "verified_at"])
            check(complete or empty, f"{b['local_id']}: partial native binding")
            if state == "not_created":
                check(empty, f"{b['local_id']}: unexpected native reference")
            if state == "published" and forge == active:
                check(complete, f"{b['local_id']}: published without verified binding")
                if complete:
                    check(isinstance(vals[nativeid], int) and vals[nativeid] > 0, f"{b['local_id']}: invalid number")
                    check(vals["url"].startswith("https://"+ ("github.com/" if forge=="github" else "gitlab.com/")), f"{b['local_id']}: invalid provider URL")
        if b["kind"] in ("child","umbrella"):
            a = b.get("execution_approval",{})
            check(a.get("scope_revision") is not None, f"{b['local_id']}: missing scope revision")
            if a.get("state") == "approved":
                check(all(a.get(k) for k in ["approved_scope_revision","approved_scope_sha256","evidence_url","approved_by","verified_at","provider"]), f"{b['local_id']}: incomplete approval metadata")
            else:
                check(a.get("state") in ("pending_approval","stale","rejected","change_requested"), f"{b['local_id']}: invalid approval state")
        # Local metadata NEVER grants permission; live provider verification mandatory.
    check(providers.get("status") == ("draft_only" if all(b["status"] == "not_created" for b in providers["bindings"]) else "partially_published"), "Provider publication summary inconsistent")
    for forge in ["github", "gitlab"]:
        exp = load(f"management/providers/{forge}_labels.draft.json")
        check(exp["status"] == "draft_not_created", f"{forge}: unexpectedly published catalog")
        check({l["name"] for l in exp["labels"]} == cset, f"{forge}: catalog diverged")
    check(not complaints["entries"] and complaints["counts"]["recorded"] == 0, "Unexpected complaint entries or count")
    check((ROOT / "COMPLAIN.md").is_file(), "COMPLAIN.md absent")
    check(wiki["metrics"].get("complaints_registered_local") == 0 and wiki["metrics"].get("complaints_escalated_verified") is None, "Wiki complaint evidence not safe")
    cfg = load("rag/fts5/config.json")
    check(cfg.get("engine") == "sqlite-fts5", "Active runtime must be SQLite FTS5")
    check("design/BYAR_BARBER_HIFI_TOP_HIERARCHY.png" in cfg["human_only"] and "design/" in cfg["exclude_paths"], "Hi-Fi exclusion missing")
    for name in ["COMPLAIN.md", "rag/complaints.json", "rag/label_assignments.json", "rag/provider_bindings.json"]:
        check(name in cfg["index_sources"], f"Missing RAG index source: {name}")
    sys.path.insert(0, str(ROOT / "tools"))
    from github_free_policy import load_policy, validate_policy
    policy = load_policy(ROOT)
    dispatch_workflow = (ROOT / '.github/workflows/agent-dispatch.yml').read_text(encoding='utf-8')
    for error in validate_policy(policy, dispatch_workflow):
        problems.append('GitHub Free private policy: '+error)
    return problems, {"milestones":len(milestones),"umbrellas":len(umbrellas),"children":len(children),"pr_plans":len(plans),"labels":len(cset),"label_assignments":len(amap),"provider_bindings":len(binding_ids),"recorded_complaints":len(complaints["entries"])}

if __name__ == "__main__":
    issues, summary = validate()
    print(json.dumps({"status":"PASS" if not issues else "FAIL","summary":summary,"issues":issues,"verification_scope":"OFFLINE STRUCTURAL ONLY"},ensure_ascii=False,indent=2))
    sys.exit(1 if issues else 0)
