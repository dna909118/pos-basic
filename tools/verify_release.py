#!/usr/bin/env python3
"""Verify release source file hashes after extraction (runtime files excluded)."""
import hashlib
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'RELEASE_SHA256.txt'

def verify():
    failed=[];entries=0
    for row in MANIFEST.read_text(encoding='utf-8').splitlines():
        if not row or row.startswith('#'):continue
        try:checksum,relative=row.split('  ',1)
        except ValueError:failed.append('Malformed manifest line');continue
        if not relative or relative.startswith('/') or '..' in Path(relative).parts:failed.append(relative);continue
        p=ROOT/relative
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=checksum:
            failed.append(relative)
        entries+=1
    return entries,failed
if __name__=='__main__':
    n,errors=verify();print(f'RELEASE INTEGRITY: {"PASS" if not errors else "FAIL"}; files={n}; mismatches={errors}')
    sys.exit(bool(errors))
