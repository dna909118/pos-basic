#!/usr/bin/env python3
"""Run a single authorized BYAR BARBER worker; artifact-only, no provider writes."""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def run(manifest,output,model,dry_run=False):
    m=json.loads(Path(manifest).read_text(encoding='utf-8'))
    if m.get('status')!='APPROVED_FOR_RUN' or m.get('dispatch_authorized') is not True or m.get('provider')!='github':
        raise ValueError('Only trusted preflight-approved manifests may execute')
    if m.get('engine') not in ['opencode','mini-swe'] or not re.fullmatch(r'CI-[A-Za-z0-9-]+',m.get('canonical_child_id','')):
        raise ValueError('Invalid worker manifest')
    if not re.fullmatch(r'[A-Za-z0-9_-]+/[A-Za-z0-9_.-]+',m.get('repository','')):
        raise ValueError('Invalid repository')
    if not re.fullmatch(r'[0-9a-f]{40}',m.get('base_sha','')):
        raise ValueError('Missing Git revision baseline')
    if len(m.get('scope_evidence',[]))!=2:
        raise ValueError('Missing separate Human approval evidence')
    if not model or not re.fullmatch(r'[A-Za-z0-9_.\-/:]+',model):
        raise ValueError('Agent model name missing or invalid')
    result=Path(output);result.mkdir(parents=True,exist_ok=True)
    task='''BYAR BARBER authorized isolated engineering task.\nChild: {child}; Umbrella: {umbrella}; Milestone: {milestone}.\nUse only the scope in the canonical draft and approved revision in the manifest. Read AGENTS.md. Do not access design/ or Human-only Hi-Fi. Do not modify unauthorized files, provider state, approvals, Issue status, or merge PR. Run relevant tests. Keep changes local for patch review.\n'''.format(child=m['canonical_child_id'],umbrella=m['umbrella_id'],milestone=m['milestone_id'])
    task += '\nApproved scope evidence is provided separately in the trusted execution manifest.\n'
    prompt_file=result/'task.txt';prompt_file.write_text(task)
    if m['engine']=='opencode':cmd=['opencode','run','--standalone','--model',model,task]
    else:cmd=['mini','-y','--exit-immediately','--model',model,'--task',task,'--output',str(result/'trajectory.traj.json')]
    report={'schema_version':'1.0','canonical_child_id':m['canonical_child_id'],'engine':m['engine'],'base_sha':m['base_sha'],'status':'NOT_RUN','returncode':None,'tests':'not_collected','pr_url':None,'merge':'not_authorized','command':[cmd[0],cmd[1]],'execution_note':'external model execution not attempted' if dry_run else ''}
    if dry_run:
        (result/'execution_result.json').write_text(json.dumps(report,indent=2)+'\n')
        return report
    # Agent may execute untrusted repository code. Only run in ephemeral job without Git write credentials.
    with (result/'worker_stdout.log').open('w') as out, (result/'worker_stderr.log').open('w') as err:
        try:
            completed=subprocess.run(cmd,cwd=ROOT,stdout=out,stderr=err,timeout=2700,env=os.environ.copy())
            report['status']='AGENT_FINISHED' if completed.returncode==0 else 'AGENT_FAILED'
            report['returncode']=completed.returncode
        except (OSError,subprocess.TimeoutExpired) as e:
            report['status']='AGENT_FAILED';report['execution_note']=type(e).__name__
    # Include new untracked files in diff, but never stage actual commit or include secrets by design.
    subprocess.run(['git','add','-N','.'],cwd=ROOT,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,check=False)
    diff=subprocess.run(['git','diff','--binary'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    (result/'changes.patch').write_bytes(diff.stdout)
    # Evidence is review-only; no push, Issue modification or PR creation.
    (result/'execution_result.json').write_text(json.dumps(report,indent=2)+'\n')
    return report

def main():
    p=argparse.ArgumentParser();p.add_argument('--manifest',required=True);p.add_argument('--out',required=True);p.add_argument('--model',required=True);p.add_argument('--dry-run',action='store_true');a=p.parse_args()
    try:
        data=run(a.manifest,a.out,a.model,a.dry_run);print(json.dumps(data,ensure_ascii=False));return 0 if data['status']!='AGENT_FAILED' else 1
    except (ValueError,OSError,KeyError,subprocess.SubprocessError) as exc:
        print(json.dumps({'status':'BLOCKED','reason':str(exc)}),file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())
