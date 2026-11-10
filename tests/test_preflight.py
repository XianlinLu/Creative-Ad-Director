from pathlib import Path
import importlib.util
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "creative-ad-director"
SCRIPT = SKILL_DIR / "scripts" / "preflight.py"


def load_module():
    spec = importlib.util.spec_from_file_location("creative_ad_director_preflight", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PreflightTests(unittest.TestCase):
    def test_skill_preflight_passes(self):
        module = load_module()
        self.assertEqual(module.validate(SKILL_DIR), [])

    def test_utf16_units_counts_non_bmp_as_two(self):
        module = load_module()
        self.assertEqual(module.utf16_units("A😀"), 3)


if __name__ == "__main__":
    unittest.main()
