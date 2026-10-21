# Flutter Web Builder — BYAR BARBER v0.0.8-r1

The **builder configuration is included in the bundle**, independently of the Flutter business application. It uses a versioned toolchain contract in `builder/flutter/toolchain.json`, `tools/flutter_builder.py`, and `.github/workflows/flutter-builder.yml`.

## Contract

- Flutter **3.44.0 stable**, Dart **3.12.0**, target **web**.
- Mix **2.2.2**, following the unchanged Design System dependency contract. Resolve on a live Flutter runner before declaring build acceptance.
- The GitHub Action installs the pinned SDK, validates version, creates a disposable smoke app **outside the repository**, resolves Mix, analyzes, tests, release-builds web and uploads `byar-flutter-builder-smoke`.
- If a separately authorized application is later committed at `app/`, the same workflow enforces its committed `pubspec.lock`, pinned Mix, runs analyze/tests/build, and uploads `byar-barber-web`.
- Generated smoke app is **not** the BYAR BARBER business app. No authentication/POS screens, fake transactions, PWA production deployment, or GitHub Pages publication is implied.
- Generic root base href `/` is configured because the target repository may change; production hosting under a subpath requires a separate reviewed config update.
- SDK/package downloads are expected during GitHub Actions execution and require network; this does not affect the offline JSON/FTS5 engine.

## Operator commands

Without Flutter installed (offline contract check):

```bash
python tools/flutter_builder.py config
python -m unittest discover -s tests -v
```

With Flutter SDK available (builder proof):

```bash
python tools/flutter_builder.py doctor
python tools/flutter_builder.py smoke --artifact-dir /tmp/byar-flutter-smoke-output
```

For a real **approved** app at `app/` with committed `pubspec.lock`:

```bash
python tools/flutter_builder.py build --app-dir app --artifact-dir /tmp/byar-product-output
```

The artifact destination must not already exist. The CLI exits nonzero for absent/mismatched SDK, missing app/lockfile, mismatched Mix version or failed build.

## Verification boundary

The source bundle can verify configuration syntax and pure-Python builder tests offline. Actual `flutter create`, Mix resolution, `flutter analyze`, `flutter test`, web compilation and GitHub Actions artifact upload require a live Flutter toolchain/runner. Do **not** mark these PASS until executed. The builder is installed/configured on first workflow run, not stored as binary SDK inside the ZIP.
