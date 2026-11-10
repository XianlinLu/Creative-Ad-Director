#!/usr/bin/env python3
"""Validate measured audio metadata before a Seedance 2.5 r2v request.

This does not measure files, submit jobs, or verify voice quality/native bindings.
"""
from __future__ import annotations

import argparse
import json
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

MIN_AUDIO = Decimal('1.8')
MAX_TOTAL = Decimal('30.2')
PREP_MIN = Decimal('2.0')
PREP_TOTAL = Decimal('30.0')


def validate_manifest(manifest: object) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    total = Decimal(0)
    if not isinstance(manifest, dict):
        return {'ready_to_submit': False, 'errors': ['manifest must be an object'],
                'warnings': [], 'total_audio_seconds': 0.0}
    if manifest.get('model') != 'dreamina-seedance-2-5' or manifest.get('mode') != 'r2v':
        errors.append('This guard applies only to dreamina-seedance-2-5 in r2v; verify other model/mode contracts separately')
    roles = manifest.get('required_roles')
    if not isinstance(roles, list) or any(not isinstance(r, str) or not r.strip() for r in roles):
        errors.append('required_roles must be a list of non-empty role IDs (empty for no native audio)')
        roles = []
    if len(set(roles)) != len(roles):
        errors.append('required_roles contains duplicate IDs')
    entries = manifest.get('audio')
    if not isinstance(entries, list):
        errors.append('audio must be a list of actual outgoing audio entries')
        entries = []
    covered: set[str] = set()
    assets: set[str] = set()
    for i, entry in enumerate(entries):
        label = f'audio[{i}]'
        if not isinstance(entry, dict):
            errors.append(f'{label} must be an object')
            continue
        role = entry.get('role_id')
        if not isinstance(role, str) or role not in roles:
            errors.append(f'{label} is not mapped to a required audible role')
        else:
            covered.add(role)
        asset = entry.get('asset_id')
        if not isinstance(asset, str) or not asset.strip():
            errors.append(f'{label} needs an actual prepared asset handle')
        elif asset in assets:
            errors.append(f'{label} repeats an attached asset; remove unnecessary duplicate bindings')
        else:
            assets.add(asset)
        if entry.get('purpose') not in {'voice_reference', 'dialogue'}:
            errors.append(f'{label} purpose must be voice_reference or dialogue')
        if entry.get('duration_verified') is not True:
            errors.append(f'{label} actual prepared-file duration has not been verified')
        if entry.get('source_approved') is not True:
            errors.append(f'{label} has no approved source voice/script provenance')
        raw = entry.get('duration_seconds')
        try:
            if isinstance(raw, bool) or not isinstance(raw, (int, float, str)):
                raise ValueError('not a duration')
            duration = Decimal(str(raw))
            if not duration.is_finite() or duration < 0:
                raise ValueError('not a finite nonnegative duration')
        except (InvalidOperation, ValueError):
            errors.append(f'{label} needs finite nonnegative measured duration_seconds')
            continue
        # Count every submitted entry, even a duplicate, just as an outgoing list.
        total += duration
        if duration < MIN_AUDIO:
            errors.append(f'{label} is {duration}s; each audio must be >= 1.8s')
        elif duration < PREP_MIN:
            warnings.append(f'{label} meets the limit but is below the 2.0s preparation margin')
    missing = sorted(set(roles) - covered)
    if missing:
        errors.append('Missing audio for required roles: ' + ', '.join(missing))
    if total > MAX_TOTAL:
        errors.append(f'Combined attached audio is {total}s; must be <= 30.2s')
    elif total > PREP_TOTAL:
        warnings.append('Combined audio meets the limit but exceeds the 30.0s preparation margin')
    return {'ready_to_submit': not errors, 'errors': errors, 'warnings': warnings,
            'total_audio_seconds': float(total)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    args = parser.parse_args()
    try:
        manifest = json.loads(args.manifest.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        print(json.dumps({'ready_to_submit': False, 'errors': [str(exc)]}), file=sys.stderr)
        return 2
    result = validate_manifest(manifest)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['ready_to_submit'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
