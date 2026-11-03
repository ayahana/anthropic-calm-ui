import importlib.util
from pathlib import Path
import subprocess
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/anthropic-calm-ui/scripts/check_contrast.py'
spec = importlib.util.spec_from_file_location('check_contrast', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ContrastTests(unittest.TestCase):
    def test_known_extremes(self):
        self.assertEqual(module.contrast('#ffffff', '#ffffff'), 1)
        self.assertEqual(module.contrast('#000000', '#ffffff'), 21)
        self.assertEqual(module.contrast('#ffffff', '#000000'), 21)

    def test_all_current_pairs(self):
        rows = module.evaluate(module.DEFAULT.read_text(encoding='utf-8'))
        self.assertEqual(len(rows), 52)
        self.assertTrue(all(row['passed'] for row in rows))

    def test_missing_theme_fails(self):
        with self.assertRaises(ValueError):
            module.evaluate(':root {}')

    def test_unsupported_color_fails(self):
        with self.assertRaises(ValueError):
            module.evaluate(module.DEFAULT.read_text(encoding='utf-8').replace('#242421', 'rgb(36 36 33)'))

    def test_duplicate_tested_hex_fails(self):
        css = module.DEFAULT.read_text(encoding='utf-8').replace(
            '--calm-text: #242421;',
            '--calm-text: #242421; --calm-text: #ffffff;')
        with self.assertRaisesRegex(ValueError, 'Duplicate tested token'):
            module.evaluate(css)

    def test_duplicate_without_final_semicolon_fails(self):
        css = module.DEFAULT.read_text(encoding='utf-8').replace(
            '--calm-duration: 140ms;',
            '--calm-duration: 140ms; --calm-text: rgb(247 246 242)')
        with self.assertRaisesRegex(ValueError, 'Duplicate tested token'):
            module.evaluate(css)

    def test_unsupported_override_exits_input_error(self):
        # The browser uses the later rgb() declaration. Never silently report
        # success using the earlier supported hex value.
        css = module.DEFAULT.read_text(encoding='utf-8').replace(
            '--calm-text: #242421;',
            '--calm-text: #242421; --calm-text: rgb(247 246 242);')
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'tokens.css'
            path.write_text(css, encoding='utf-8')
            result = subprocess.run(
                [sys.executable, str(SCRIPT), '--tokens', str(path)],
                capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertNotIn('52/52 passed', result.stdout)
            self.assertIn('Duplicate tested token', result.stderr)

    def test_standalone_skill_install(self):
        with tempfile.TemporaryDirectory() as folder:
            installed = Path(folder) / 'anthropic-calm-ui'
            shutil.copytree(ROOT / 'skills/anthropic-calm-ui', installed,
                            ignore=shutil.ignore_patterns('__pycache__'))
            result = subprocess.run(
                [sys.executable, str(installed / 'scripts/check_contrast.py')],
                cwd=folder, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('52/52 passed', result.stdout)

    def test_repository_entrypoint(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / 'scripts/check_contrast.py')],
            cwd=tempfile.gettempdir(), capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('52/52 passed', result.stdout)

    def test_regression_exits_nonzero(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'tokens.css'
            path.write_text(module.DEFAULT.read_text(encoding='utf-8').replace(
                '--calm-text: #242421;', '--calm-text: #f7f6f2;'), encoding='utf-8')
            result = subprocess.run([sys.executable, str(SCRIPT), '--tokens', str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('FAIL light text/canvas', result.stdout)


if __name__ == '__main__':
    unittest.main()
