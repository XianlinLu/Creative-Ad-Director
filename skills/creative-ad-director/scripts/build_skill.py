#!/usr/bin/env python3
"""Build a deterministic Lumina import ZIP after static validation."""

from __future__ import annotations

import argparse
import importlib.util
import sys
import zipfile
from pathlib import Path


def load_preflight(script: Path):
    spec = importlib.util.spec_from_file_location("creative_ad_director_preflight", script)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {script}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(skill_dir: Path, output: Path) -> None:
    preflight = load_preflight(skill_dir / "scripts" / "preflight.py")
    errors = preflight.validate(skill_dir)
    if errors:
        raise RuntimeError("preflight failed:\n" + "\n".join(errors))

    included = [skill_dir / "SKILL.md", skill_dir / "agents" / "openai.yaml"]
    included.extend(sorted((skill_dir / "references").glob("*.md")))

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in included:
            info = zipfile.ZipInfo(path.relative_to(skill_dir).as_posix())
            info.date_time = (2020, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skill-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        build(args.skill_dir.resolve(), args.output.resolve())
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(f"Built {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
