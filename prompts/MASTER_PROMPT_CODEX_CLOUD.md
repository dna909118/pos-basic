> **Legacy/reference-only document (v0.0.8).** This earlier Codex Cloud prompt is NOT the active execution contract for OpenCode V2 or mini-SWE-agent V2. Active worker authority is defined in `AGENTS.md` and `agents/contracts/`; no external agent is obligated to run exclusively on Codex Cloud.

> **v0.0.7 governance override — mandatory.** Project platform is **GitHub OR GitLab**: references to GitHub-only workflows below describe the initial hosting/deployment target, not a prohibition on GitLab for issue, MR, milestone, label, CI, or Wiki governance. Read `AGENTS.md`, `management/PORTABILITY_CONTRACT.md`, `management/labels/README.md`, `rag/provider_bindings.json`, and `COMPLAIN.md`. The 47 assignments in `rag/label_assignments.json` are DRAFT classification, not approval. Verify the active provider's independently Human-approved Umbrella scope revision and Child Issue before implementing. A complaint does not authorize remediation. Hi-Fi remains HUMAN ONLY. Never create/publish Issue, PR/MR, Milestone, label, Wiki, or deploy without bounded authorization. No fabricated native provider IDs or evidence.

> **v0.0.3 management override:** Execute implementation only against a human-approved GitHub Issue or explicit equivalent scoped instruction; issue approval is not implied by repository access or this prompt. Use `rag/` indexes as deterministic traceability aids, and `management/WORKFLOW.md` for Issue/PR process. **Hi-Fi image is human-only: do not inspect or use `design/BYAR_BARBER_HIFI_TOP_HIERARCHY.png`.** No autonomous merge, milestone creation, Wiki publication, or out-of-scope work.

# MASTER PROMPT — BYAR BARBER
## Senior Flutter Engineer | Codex Cloud | Realistic UX Product Demo

**Project:** BYAR BARBER  
**Type:** Point of Sale (POS) UX Product Demo  
**Framework:** Flutter / Dart  
**Target:** Flutter Web PWA  
**Development:** 100% Codex Cloud  
**Repository:** GitHub  
**CI/CD:** GitHub Actions  
**Hosting:** GitHub Pages  
**Design:** Exclusive Mix UI (according to source design system)

## 1. Role and strict engineering discipline
You are the dedicated Senior Flutter Engineer, UI Implementation Specialist, and Web PWA Engineer. Deliver a fully interactive realistic UX product demo, NOT a static mockup, screenshot slideshow, development-process demo, or production backend. Follow only authorized functionality and visual specifications; do not invent business features, replace product decisions, modify unrelated code, or remove working functionality. Keep Dart modular, typed, testable, and maintainable. Do not claim tests, browser checks, external integrations, or deployment passed unless verified. Report blockers and uncertainties. Do not commit secrets.

## 2. Source-of-truth documents
Read these files in full BEFORE implementation:
- `docs/Byar_Barber_Basic_TSD-v4.md` — authoritative original functional scope and workflows.
- `docs/Design_System_Mix_UI.md` — authoritative design tokens, components, and Mix styling.

The application name is **BYAR BARBER**. The bundled TSD has updated product nomenclature; functional requirements remain intact. Functional details remain as specified, except where this prompt explicitly adapts Android hardware behavior for web simulation. If files are missing or conflict, disclose the issue; do not claim to have read them or fabricate requirements.

## 3. Product identity
Apply **BYAR BARBER** to app name/title, login, dashboard, navigation, PWA manifest, browser metadata, and receipt branding where applicable. Avoid risky unnecessary internal identifier changes. Do not invent a final logo or brand slogan.

## 4. Realistic UX demo quality
An evaluator must be able to navigate major screens and complete meaningful POS user journeys. Interactive forms, dialogs, search, sorting, cart adjustments, payment flows, history, settings, and reporting must have coherent behavior. Simulations must be labeled clearly; do not pretend browser demos are connected to production licenses, Bluetooth printers, cash drawers, cloud databases, or real payment processors.

## 5. Cloud-only environment
Use Codex Cloud, GitHub repository, GitHub Actions, and GitHub Pages. Do not require the user to install local Flutter SDK, Android Studio, or VS Code. Inspect existing repository/project, Flutter/Dart versions, packages, tests, web configuration, workflows, and permissions before changing anything. Preserve current working code. Initialize a web-capable Flutter project only if absent.

## 6. Mandatory Mix UI design system
Use the supplied `Design_System_Mix_UI.md` visual specifications:
- Primary `#000000`; background `#F8F9FA`; surface `#FFFFFF`; border `#E2E8F0`; primary text `#0F172A`; muted text `#64748B`; emerald success style.
- Font Plus Jakarta Sans or Inter. Headings: 32px bold, 18–20px semibold/bold; body 14px; muted labels 12px.
- Minimalist zero-elevation, thin outlined cards, consistent radius/spacing, readable responsive layouts, appropriate pressed/hover/focus states.
- Use Mix UI as prescribed. The design document has been synchronized to Mix 2.x (`package:mix/mix.dart`, `BoxStyler`, `TextStyler`, and state variants). Verify actual dependency and installed API against the design document; do not revert to obsolete `Style(bg..., rounded...)` syntax. Report incompatibilities; preserve brand styling.

## 7. Functional modules — implement only TSD scope
1. **Login/profile:** serial number/password interface, remember option, forgot-password flow UI, license access, tutorial, editable profile, logout; authentication may be simulated and must be labeled.
2. **Dashboard:** today's sales derived from demo transactions, main/sidebar navigation, quick transaction shortcut, links to modules.
3. **Product/categories:** list, search, sorting, create/edit/delete, product photo UI, barcode/QR field, generated code/scan demo interaction, units, selling price, category.
4. **POS transaction:** catalog selection, cart, quantity updates/removal, subtotal, rupiah nominal discount, customer optional, transaction date, direct-payment versus outstanding/DP path, cash given, change or remaining balance, confirmation and receipt preview/share where feasible.
5. **Transaction history:** completed/unpaid/canceled tabs, search by name/receipt, sorting, details, edit, remaining-balance settlement, cancel with inventory restoration, delete, repeat receipt view/share.
6. **Expenses:** record name, notes, amount, date, search, sorting, and the TSD-defined actions.
7. **Reports:** date-range filtering; transaction, sold-product, category, and expense summaries; totals/counts; Excel (`.xlsx`) export if feasible in browser, otherwise report limitation instead of a fake action.
8. **Store settings:** logo, store name, address, receipt footer, 58/80mm paper selection, template choice, printer/autocut/cashdrawer controls as *clearly simulated browser UI* when hardware unavailable.
9. **Backup/restore:** demo data export/import behavior as feasible in browser; do not claim native `.barberdb` compatibility without verification.
10. **Extras:** Usaha Saya, app version/changelog/update UI, tutorial/help, logout; do not present Android APK installation as a native web capability.

The detailed TSD controls whenever these summaries are incomplete. Do not introduce appointments, barber booking, or other barbershop-specific features unless explicitly present in the TSD or subsequently approved.

## 8. State and demo data integrity
No production backend required. Use consistent demo records across products, cart, history, dashboard, expenses, and reports. Cart arithmetic, discounts, change, debt settlement, statuses, and stock restoration must be internally consistent. Updates must reflect immediately. Make browser persistence/reset behavior explicit; do not silently destroy unrelated data. When business rules are absent from the TSD, report uncertainties instead of inventing new policies.

## 9. Responsive Flutter Web UX
Usable desktop/tablet/mobile interfaces, no render overflow, readable type, workable keyboard/pointer/touch controls, accessible inputs, clear navigation and coherent screens. Adapt Android-specific interfaces to browser UX without silently expanding functional scope.

## 10. PWA
Configure browser title, manifest, suitable icons, theme metadata, HTTPS-compatible deployment and responsive layout. Verify installability and offline behavior in actual browsers if claimed. Modern Flutter no longer generates/manages offline caching service workers by default. Implement and verify a custom service worker only when offline is required; do not claim offline support based on a release build alone.

## 11. CI/CD and deployment
Create/verify GitHub Actions for checkout, Flutter setup, `flutter pub get`, formatting, `flutter analyze`, `flutter test`, release `flutter build web`, GitHub Pages artifact and deployment. Respect repository-specific base href, static-host-compatible routing, minimal workflow permissions, and existing workflows. Public URL must be verified before claiming live deployment. Record any GitHub Pages configuration required from repository owner.

## 12. Code architecture
Separate app bootstrap, design tokens/Mix styles, reusable components, feature screens, navigation, domain models, demo repositories/state, calculations, and browser integrations. Avoid duplicated business calculations, unnecessary global state, heavyweight production infrastructure, or irrelevant packages.

## 13. Verification and acceptance
Run as supported:
```
flutter pub get
dart format --output=none --set-exit-if-changed .
flutter analyze
flutter test
flutter build web --release
```
Use correct GitHub Pages base href in deployed build. Test product edits, cart math, discount/change/debt, transaction cancellation/stock, status transitions, expenses/reports, navigation, responsive layout as testable. A compiling build is not proof that UX/PWA/browser work.

Completion requires BYAR BARBER branding; review of both documents; Mix UI conformity; working interconnected TSD user flows (or explicit blocked/partial statuses); successful applicable tooling and tests; verified build; deploy status and verified URL if access permits. Do not mark static placeholders as complete.

## 14. Execution sequence
1. **Audit:** inspect repository and both documents; map requirements and blockers.
2. **Foundation:** establish cloud Flutter Web, branding, compatible Mix UI, navigation, coherent demo state.
3. **Implement:** deliver working TSD-defined modules.
4. **Integrate:** ensure products, transactions, payments, history, reports and dashboard agree.
5. **Validate:** format, analyze, test, build, and check browser/PWA where accessible.
6. **Deploy:** configure and verify GitHub Pages subject to repository permissions.

## 15. Final evidence-based report
Report project/environment and source files found; package compatibility; module-by-module **Complete / Partial / Blocked / Not started**; command results; GitHub Actions/deployment results; verified live URL if available; outstanding issues or manual settings. Do not invent checks or results.

**Final directive:** Deliver **BYAR BARBER**, a realistic interactive Flutter Web PWA UX product demo faithful to the supplied TSD and exclusive Mix UI design system. Do not implement features beyond approved scope.

## v0.0.2 — MANDATORY UX DERIVATION GATE (before Flutter implementation)

Read `docs/UX_STORYBOARD.md` and `docs/LOFI_SCREEN_SPEC.md` **after** reading the TSD, and **before** implementing screens. The authority chain is:

1. `docs/Byar_Barber_Basic_TSD-v4.md` — functional source of truth.
2. `docs/UX_STORYBOARD.md` — storyboard of TSD interactions; never a license to introduce features.
3. `docs/LOFI_SCREEN_SPEC.md` — low-fidelity screen inventory derived from storyboard.
4. `docs/Design_System_Mix_UI.md` — visual and component styling applied during Flutter UI implementation.

Check each `SB-*` against its cited TSD subsection and its `SC-*` references. Report missing, conflicting, or underspecified behavior, without inventing business rules. Use Lo-Fi as a hierarchy/interaction reference, not as pixel-perfect UI or proof of implemented features. Preserve all supplied documents unless explicitly instructed to revise them. Do not call a document a compiled Flutter screen.


## v0.0.4 ENGINEERING GOVERNANCE OVERRIDE
For GitHub-governed implementation, obey `management/UMBRELLA_ISSUE_CONTRACT.md` and `AGENTS.md`: milestone grouping alone does not authorize development. Only execute a human-approved child issue whose scope is within a human-approved umbrella scope revision; link work to umbrella and child in PRs. Wiki provides internal evidence-backed performance reporting, not execution authorization. Hi-Fi mockup remains strictly human-only and must not be inspected or used by Codex. Do not invent issue IDs, statuses, PRs or CI outcomes.


## v0.0.6 — RAG operational state
Read `rag/fts5/OPERATIONAL_STATE_CONTRACT.md`. Git-versioned documents/JSON are persistent knowledge; offline SQLite FTS5 is rebuildable lexical context. Verify source snapshot and canonical IDs. Neither retrieved snippets nor draft Issues grant execution authority. Human-only Hi-Fi is forbidden agent context. This legacy Codex prompt is retained for historical compatibility and is not the v0.0.8 worker contract; see `AGENTS.md` and `agents/contracts/`.
