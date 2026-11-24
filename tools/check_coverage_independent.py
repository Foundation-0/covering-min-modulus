#!/usr/bin/env python3
"""Exact independent covering check by recursive residue-class refinement."""
import argparse,math,re,sys

def verify(filename,max_nodes=1000000):
 rows=[];header=None
 with open(filename)as f:
  for raw in f:
   s=raw.strip()
   if not s:continue
   if s.startswith('#'):
    parts=s[1:].strip().split(':',1)
    if len(parts)==2 and parts[0]=='minimum modulus':header=int(parts[1])
    continue
   bits=s.split()
   if len(bits)!=3 or bits[1]!='mod' or not re.fullmatch('[0-9]+',bits[0])or not re.fullmatch('[0-9]+',bits[2]):raise ValueError('bad row')
   residue,modulus=int(bits[0]),int(bits[2])
   if modulus<2 or residue not in range(modulus):raise ValueError('bad integer range')
   if any(m==modulus for a,m in rows):raise ValueError('repeated modulus')
   rows.append((residue,modulus))
 if not rows or header!=min(m for a,m in rows):raise ValueError('missing or inconsistent minimum modulus')
 pending=[(0,1)];nodes=0
 while pending:
  r,step=pending.pop();nodes+=1
  if nodes>max_nodes:raise ValueError('node cap exceeded; coverage not decided')
  # Every integer in this class is r+step*t.
  candidates=[(a,m)for a,m in rows if (a-r)%math.gcd(step,m)==0]
  if any(step%m==0 and r%m==a for a,m in candidates):continue
  if not candidates:raise ValueError(f'uncovered class: {r} modulo {step}')
  a,m=min(candidates,key=lambda row:row[1]//math.gcd(step,row[1]))
  factor=m//math.gcd(step,m)
  if factor<=1:raise ValueError('refinement did not advance')
  if nodes+len(pending)+factor>max_nodes:raise ValueError('node cap exceeded; coverage not decided')
  pending.extend((r+step*t,step*factor)for t in range(factor))
 return {'covered':True,'nodes':nodes}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('file');p.add_argument('--max-nodes',type=int,default=1000000);a=p.parse_args()
 try:print(verify(a.file,a.max_nodes))
 except (ValueError,OSError)as e:print(e,file=sys.stderr);return 1
 return 0
if __name__=='__main__':sys.exit(main())
