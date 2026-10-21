#!/usr/bin/env python3
"""BYAR BARBER Flutter Web builder. No business app is generated in the repository.

`config` works offline without Flutter; `doctor`, `smoke`, `build` require Flutter.
Smoke generates an isolated temporary Flutter project; actual application builds
require an existing, separately approved `app/` with a committed pubspec.lock.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_FILE = ROOT / 'builder/flutter/toolchain.json'

class BuilderError(Exception):
    pass


def load_config(path=CONFIG_FILE):
    try:
        config = json.loads(Path(path).read_text(encoding='utf-8'))
    except (ValueError, OSError) as exc:
        raise BuilderError(f'Invalid builder configuration: {exc}') from exc
    required = ('flutter_version', 'flutter_channel', 'dart_version_prefix', 'mix_version',
                'application_directory', 'smoke_project_name', 'web_base_href')
    if any(not isinstance(config.get(k), str) or not config[k] for k in required):
        raise BuilderError('Missing or invalid Flutter builder configuration key')
    for k in ('flutter_version', 'dart_version_prefix', 'mix_version'):
        if not re.fullmatch(r'\d+\.\d+\.\d+', config[k]):
            raise BuilderError(f'Invalid pinned version for {k}')
    if config['flutter_channel'] != 'stable':
        raise BuilderError('This bundle requires the stable Flutter channel')
    if not re.fullmatch(r'[a-z][a-z0-9_]*', config['smoke_project_name']):
        raise BuilderError('Unsafe Flutter smoke project name')
    if not config['web_base_href'].startswith('/') or not config['web_base_href'].endswith('/') or '\n' in config['web_base_href']:
        raise BuilderError('Invalid web base href')
    if Path(config['application_directory']).is_absolute() or '..' in Path(config['application_directory']).parts:
        raise BuilderError('Unsafe application directory')
    return config


def execute(args, cwd=None):
    try:
        subprocess.run(args, cwd=cwd, check=True, text=True)
    except FileNotFoundError as exc:
        raise BuilderError(f'Executable missing: {args[0]}') from exc
    except subprocess.CalledProcessError as exc:
        raise BuilderError(f'Command failed ({exc.returncode}): {args!r}') from exc


def flutter_metadata():
    try:
        # Flutter may perform first-run setup before its machine-readable output.
        subprocess.run(['flutter', '--version'], check=True, text=True, capture_output=True)
        p = subprocess.run(['flutter', '--version', '--machine'], check=True, text=True,
                           capture_output=True)
    except FileNotFoundError as exc:
        raise BuilderError('Flutter SDK not installed or not on PATH') from exc
    except subprocess.CalledProcessError as exc:
        raise BuilderError(f'Flutter version inspection failed: {exc.stderr[-500:]}') from exc
    try:
        return json.loads(p.stdout)
    except ValueError as exc:
        raise BuilderError('Flutter --version --machine returned invalid JSON') from exc


def check_toolchain(config, metadata):
    actual = metadata.get('frameworkVersion', '')
    dart = metadata.get('dartSdkVersion', '')
    if actual != config['flutter_version']:
        raise BuilderError(f'Flutter mismatch: expected {config["flutter_version"]}, actual {actual}')
    if not dart.startswith(config['dart_version_prefix']):
        raise BuilderError(f'Dart mismatch: expected {config["dart_version_prefix"]}, actual {dart}')
    return {'flutter': actual, 'dart': dart, 'match': True}


def insert_mix_dependency(pubspec_text, version):
    lines = pubspec_text.splitlines(keepends=True)
    start = next((i for i, line in enumerate(lines) if line.rstrip() == 'dependencies:'), None)
    if start is None:
        raise BuilderError('Generated pubspec.yaml has no dependencies section')
    end = next((i for i in range(start + 1, len(lines)) if lines[i] and not lines[i].startswith((' ', '#', '\n'))), len(lines))
    if any(re.match(r'\s+mix\s*:', line) for line in lines[start + 1:end]):
        raise BuilderError('Unexpected existing mix dependency in smoke fixture')
    lines.insert(end, f'  mix: {version}\n')
    return ''.join(lines)


def copy_artifact(build_web, output_dir):
    if not (build_web / 'index.html').is_file():
        raise BuilderError('Flutter web build produced no index.html')
    output_dir = Path(output_dir).resolve()
    if output_dir.exists():
        raise BuilderError(f'Artifact destination already exists: {output_dir}')
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(build_web, output_dir)
    return {'artifact_dir': str(output_dir), 'index_html': True}


def smoke(config, artifact_dir):
    check_toolchain(config, flutter_metadata())
    with tempfile.TemporaryDirectory(prefix='byar-flutter-smoke-') as temp:
        project = Path(temp) / config['smoke_project_name']
        execute(['flutter', 'create', '--platforms=web', '--project-name',
                 config['smoke_project_name'], str(project)])
        pubspec = project / 'pubspec.yaml'
        if not pubspec.is_file():
            raise BuilderError('Flutter create did not produce pubspec.yaml')
        pubspec.write_text(insert_mix_dependency(pubspec.read_text(encoding='utf-8'),
                                                  config['mix_version']), encoding='utf-8')
        execute(['flutter', 'pub', 'get'], cwd=project)
        execute(['flutter', 'analyze', '--no-pub'], cwd=project)
        if (project / 'test').is_dir():
            execute(['flutter', 'test', '--no-pub'], cwd=project)
        execute(['flutter', 'build', 'web', '--release', '--no-pub',
                 '--base-href', config['web_base_href']], cwd=project)
        result = copy_artifact(project / 'build/web', artifact_dir)
    return {'mode': 'smoke', 'flutter': config['flutter_version'],
            'mix': config['mix_version'], **result}


def build_app(config, app_dir, artifact_dir):
    check_toolchain(config, flutter_metadata())
    directory = Path(app_dir).resolve()
    if not directory.is_relative_to(ROOT.resolve()):
        raise BuilderError('App directory must be inside the repository')
    if not (directory / 'pubspec.yaml').is_file():
        raise BuilderError(f'Flutter app pubspec.yaml missing in {directory}')
    if not (directory / 'pubspec.lock').is_file():
        raise BuilderError('Flutter application must commit pubspec.lock before CI build')
    pubspec = (directory / 'pubspec.yaml').read_text(encoding='utf-8')
    if not re.search(r'^\s+mix:\s*[\"\']?' + re.escape(config['mix_version']) + r'[\"\']?\s*$', pubspec, re.MULTILINE):
        raise BuilderError(f'Application must pin mix: {config["mix_version"]}')
    execute(['flutter', 'pub', 'get', '--enforce-lockfile'], cwd=directory)
    execute(['flutter', 'analyze', '--no-pub'], cwd=directory)
    if (directory / 'test').is_dir():
        execute(['flutter', 'test', '--no-pub'], cwd=directory)
    execute(['flutter', 'build', 'web', '--release', '--no-pub',
             '--base-href', config['web_base_href']], cwd=directory)
    result = copy_artifact(directory / 'build/web', artifact_dir)
    return {'mode': 'application', 'flutter': config['flutter_version'],
            'mix': config['mix_version'], **result}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('config')
    commands.add_parser('doctor')
    smoke_cmd = commands.add_parser('smoke')
    smoke_cmd.add_argument('--artifact-dir', required=True)
    app_cmd = commands.add_parser('build')
    app_cmd.add_argument('--app-dir', default=None)
    app_cmd.add_argument('--artifact-dir', required=True)
    args = parser.parse_args(argv)
    try:
        config = load_config()
        if args.command == 'config':
            result = {'valid': True, 'config': config}
        elif args.command == 'doctor':
            result = check_toolchain(config, flutter_metadata())
        elif args.command == 'smoke':
            result = smoke(config, args.artifact_dir)
        else:
            app_dir = args.app_dir if args.app_dir is not None else ROOT / config['application_directory']
            result = build_app(config, app_dir, args.artifact_dir)
        print(json.dumps({'status': 'PASS', **result}, ensure_ascii=False, indent=2))
        return 0
    except BuilderError as exc:
        print(json.dumps({'status': 'FAIL', 'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
