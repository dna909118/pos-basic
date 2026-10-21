"""No-Flutter/offline unit tests for pinned builder contract and safety rules."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('flutter_builder_under_test', ROOT / 'tools/flutter_builder.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class FlutterBuilderTests(unittest.TestCase):
    def setUp(self):
        self.config = mod.load_config()

    def test_source_config_is_valid(self):
        self.assertEqual(self.config['flutter_version'], '3.44.0')
        self.assertEqual(self.config['mix_version'], '2.2.2')

    def test_accepts_expected_sdk_metadata(self):
        self.assertTrue(mod.check_toolchain(self.config, {
            'frameworkVersion': '3.44.0', 'dartSdkVersion': '3.12.0 (stable)'} )['match'])

    def test_rejects_mismatched_flutter(self):
        with self.assertRaises(mod.BuilderError):
            mod.check_toolchain(self.config, {'frameworkVersion':'3.43.0','dartSdkVersion':'3.12.0'})

    def test_rejects_mismatched_dart(self):
        with self.assertRaises(mod.BuilderError):
            mod.check_toolchain(self.config, {'frameworkVersion':'3.44.0','dartSdkVersion':'3.11.0'})

    def test_mix_dependency_exact_version(self):
        source='name: smoke\ndependencies:\n  flutter:\n    sdk: flutter\ndev_dependencies:\n  flutter_test:\n    sdk: flutter\n'
        result=mod.insert_mix_dependency(source, self.config['mix_version'])
        self.assertIn('  mix: 2.2.2\n', result)
        self.assertIn('dev_dependencies:',result)

    def test_reject_duplicate_mix(self):
        with self.assertRaises(mod.BuilderError):
            mod.insert_mix_dependency('dependencies:\n  mix: 2.2.2\n', '2.2.2')

    def test_reject_unsafe_app_path(self):
        with tempfile.TemporaryDirectory() as temp:
            config=self.config.copy()
            config['application_directory']='../../foo'
            p=Path(temp)/'config.json'
            p.write_text(json.dumps(config),encoding='utf-8')
            with self.assertRaises(mod.BuilderError):mod.load_config(p)

    def test_missing_sdk_raises_explicitly(self):
        with patch.object(mod.subprocess, 'run', side_effect=FileNotFoundError):
            with self.assertRaises(mod.BuilderError):mod.flutter_metadata()

    def test_missing_app_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)
            with patch.object(mod,'flutter_metadata',return_value={
                'frameworkVersion':'3.44.0','dartSdkVersion':'3.12.0'}):
                with self.assertRaises(mod.BuilderError):
                    mod.build_app(self.config,p,p/'out')

    def test_agent_runner_has_flutter_builder(self):
        workflow = (ROOT / '.github/workflows/agent-dispatch.yml').read_text(encoding='utf-8')
        self.assertIn("flutter-version: '3.44.0'", workflow)
        self.assertIn('python tools/flutter_builder.py doctor', workflow)

    def test_artifact_requires_index(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)
            (p/'build').mkdir()
            with self.assertRaises(mod.BuilderError):mod.copy_artifact(p/'build',p/'out')

if __name__=='__main__':unittest.main()
