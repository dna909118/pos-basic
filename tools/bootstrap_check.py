#!/usr/bin/env python3
"""Offline source-only self-test for the clean BYAR BARBER bundle."""
import json
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
checks=[
 ['tools/validate_governance.py'],
 ['tools/flutter_builder.py','config'],
 ['-m','unittest','discover','-s','tests','-v'],
 ['rag/fts5/operational_index.py','build'],
 ['rag/fts5/operational_index.py','status'],
 ['rag/fts5/operational_index.py','lookup','REF-SB-16'],
 ['rag/fts5/operational_index.py','query','pembayaran DP pelunasan','--top-k','3'],
]
results=[]
for args in checks:
 p=subprocess.run([sys.executable,*args],cwd=ROOT,capture_output=True,text=True)
 results.append({'command':'python '+' '.join(args),'status':'PASS' if p.returncode==0 else 'FAIL','exit_code':p.returncode,'stdout_tail':p.stdout[-700:],'stderr_tail':p.stderr[-700:]})
 if p.returncode:break
print(json.dumps({'status':'PASS' if len(results)==len(checks) and all(r['status']=='PASS' for r in results) else 'FAIL','checks':results},indent=2,ensure_ascii=False))
sys.exit(0 if len(results)==len(checks) and all(r['status']=='PASS' for r in results) else 1)
