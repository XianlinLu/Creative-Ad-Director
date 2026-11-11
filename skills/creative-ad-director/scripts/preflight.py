#!/usr/bin/env python3
"""Static validation for the Lumina Creative Ad Director import tree."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_REFERENCES = {
    "product-research.md",
    "canvas-artifacts.md",
    "creative-strategy.md",
    "production-workflow.md",
    "compliance-and-qc.md",
    "assets-and-voices.md",
    "model-routing.md",
    "autonomous-runner.md",
    "r2v-audio.md",
    "shot-prompt-compiler.md",
    "reference-rhythm.md",
}


SUPPORTED_IMPORT_EXTENSIONS = {".md", ".txt", ".json", ".yaml", ".yml"}


def import_files(skill_dir: Path) -> list[Path]:
    """Only documents and metadata belong in the Lumina import artifact."""
    files = [skill_dir / "SKILL.md", skill_dir / "agents" / "openai.yaml"]
    files.extend(sorted(p for p in (skill_dir / "references").rglob("*") if p.is_file()))
    return files


def validate_import_path(relative: Path) -> list[str]:
    errors = []
    if relative.is_absolute() or any(part in {".", ".."} for part in relative.parts):
        return [f"unsafe import path: {relative}"]
    if relative.suffix not in SUPPORTED_IMPORT_EXTENSIONS:
        errors.append(f"unsupported import extension: {relative}")
    for i, part in enumerate(relative.parts):
        name = Path(part).stem if i == len(relative.parts) - 1 else part
        if len(part) > 64 or not re.fullmatch(r"[A-Za-z0-9_-]+", name):
            errors.append(f"invalid import name (ASCII letters/digits/underscore/hyphen, max 64): {relative}")
    return errors


def utf16_units(text: str) -> int:
    return len(text.encode("utf-16-le")) // 2


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill = skill_dir / "SKILL.md"
    agent = skill_dir / "agents" / "openai.yaml"
    refs = skill_dir / "references"

    for required in (skill, agent, refs):
        if not required.exists():
            errors.append(f"missing required path: {required.relative_to(skill_dir)}")

    if not skill.exists():
        return errors

    text = skill.read_text(encoding="utf-8")
    if "TODO" in text or "[TODO" in text:
        errors.append("SKILL.md contains unfinished TODO text")
    if not re.search(r"(?m)^name:\s*creative-ad-director\s*$", text):
        errors.append("SKILL.md has the wrong or missing name")
    if not re.search(r"(?m)^description:\s*\S", text):
        errors.append("SKILL.md is missing a non-empty description")

    actual_refs = {path.name for path in refs.glob("*.md")} if refs.exists() else set()
    missing_refs = REQUIRED_REFERENCES - actual_refs
    if missing_refs:
        errors.append("missing references: " + ", ".join(sorted(missing_refs)))

    for target in re.findall(r"\]\((references/[^)#]+\.md)\)", text):
        if not (skill_dir / target).exists():
            errors.append(f"broken SKILL.md reference: {target}")

    for path in sorted(skill_dir.rglob("*.md")):
        body = path.read_text(encoding="utf-8")
        if utf16_units(body) > 30_000:
            errors.append(
                f"{path.relative_to(skill_dir)} exceeds 30,000 UTF-16 units: "
                f"{utf16_units(body)}"
            )
        if "[TODO" in body:
            errors.append(f"{path.relative_to(skill_dir)} contains unfinished TODO text")

    for path in import_files(skill_dir):
        errors.extend(validate_import_path(path.relative_to(skill_dir)))
        if path.is_symlink() or not path.resolve().is_relative_to(skill_dir.resolve()):
            errors.append(f"import file must stay inside the skill: {path.relative_to(skill_dir)}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "skill_dir",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    args = parser.parse_args()
    errors = validate(args.skill_dir.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {args.skill_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
