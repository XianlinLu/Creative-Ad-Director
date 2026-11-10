"""Regression coverage for Lumina's document-only Skill importer."""
from pathlib import Path
import importlib.util
import shutil
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/creative-ad-director'
spec = importlib.util.spec_from_file_location('package_builder', SKILL / 'scripts/build_skill.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
preflight = builder.load_preflight(SKILL / 'scripts/preflight.py')


class ImportPackageTests(unittest.TestCase):
    def test_package_is_document_only_and_self_contained(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / 'skill.zip'
            builder.build(SKILL, out)
            with zipfile.ZipFile(out) as archive:
                self.assertIsNone(archive.testzip())
                self.assertIn('SKILL.md', archive.namelist())
                self.assertIn('references/r2v-audio.md', archive.namelist())
                for name in archive.namelist():
                    self.assertIn(Path(name).suffix, {'.md', '.txt', '.json', '.yaml', '.yml'})
                    self.assertNotIn('scripts', Path(name).parts)
                    self.assertEqual(archive.read(name), (SKILL / name).read_bytes())
                unpacked = Path(d) / 'unpacked'
                archive.extractall(unpacked)
            self.assertEqual(preflight.validate(unpacked), [])

    def test_accidental_python_reference_blocks_build(self):
        with tempfile.TemporaryDirectory() as d:
            source = Path(d) / 'skill'
            shutil.copytree(SKILL, source)
            (source / 'references' / 'accidental.py').write_text('print(1)')
            out = Path(d) / 'invalid.zip'
            with self.assertRaisesRegex(RuntimeError, 'unsupported import extension'):
                builder.build(source, out)
            self.assertFalse(out.exists())

    def test_rejects_importer_incompatible_names_and_extensions(self):
        for name in ['references/voice notes.md', 'references/音频.md',
                     'references/audio.MD', 'references/' + 'a' * 65 + '.md',
                     'references/wrong.dir/audio.md', '../outside.md', '/outside.md']:
            with self.subTest(name=name):
                self.assertTrue(preflight.validate_import_path(Path(name)))

    def test_accepts_supported_lowercase_extensions(self):
        for name in ['SKILL.md', 'references/audio-rules.txt', 'references/audio_guard.json',
                     'agents/openai.yaml', 'references/Voice_2.yml']:
            self.assertEqual(preflight.validate_import_path(Path(name)), [], name)

    def test_rebuild_is_deterministic(self):
        with tempfile.TemporaryDirectory() as d:
            first, second = Path(d) / 'a.zip', Path(d) / 'b.zip'
            builder.build(SKILL, first)
            builder.build(SKILL, second)
            self.assertEqual(first.read_bytes(), second.read_bytes())


if __name__ == '__main__':
    unittest.main()
