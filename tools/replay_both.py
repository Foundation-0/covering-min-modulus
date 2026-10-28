"""Run two explicitly supplied checker scripts and preserve their evidence."""
import argparse,ast,hashlib,json,pathlib,subprocess,sys,time

def replay(system,checkers,timeout=30):
    if len(checkers)!=2 or pathlib.Path(checkers[0]).resolve()==pathlib.Path(checkers[1]).resolve():raise ValueError('two distinct checker paths required')
    result=dict(input_sha256=hashlib.sha256(pathlib.Path(system).read_bytes()).hexdigest(),checks=[])
    for checker in checkers:
        cmd=[sys.executable,str(pathlib.Path(checker).resolve()),str(pathlib.Path(system).resolve())];start=time.monotonic()
        try:
            p=subprocess.run(cmd,capture_output=True,text=True,timeout=timeout)
            try: verdict=ast.literal_eval(p.stdout.strip())
            except (ValueError,SyntaxError):verdict=None
            row=dict(command=cmd,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr,verdict=verdict,seconds=time.monotonic()-start)
        except subprocess.TimeoutExpired:row=dict(command=cmd,status='timeout',seconds=time.monotonic()-start)
        row['checker_sha256']=hashlib.sha256(pathlib.Path(checker).read_bytes()).hexdigest();result['checks'].append(row)
    result['status']='both_accept' if all(r.get('returncode')==0 and isinstance(r.get('verdict'),dict) and r['verdict'].get('covered') is True for r in result['checks']) else 'unresolved'
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('system');p.add_argument('checker1');p.add_argument('checker2');p.add_argument('--timeout',type=float,default=30);p.add_argument('--output',required=True);a=p.parse_args();r=replay(a.system,[a.checker1,a.checker2],a.timeout);pathlib.Path(a.output).write_text(json.dumps(r,indent=2)+'\n');raise SystemExit(0 if r['status']=='both_accept' else 2)
