#!/usr/bin/env python3
"""Exact covering check by a full residue-period bitmap, with an explicit cap."""
import argparse,math,re,sys

def check(path,cap=1000000):
 pairs=[];minimum=None
 for line in open(path):
  line=line.strip()
  if not line:continue
  if line.startswith('#'):
   if line.startswith('# minimum modulus:'):minimum=int(line.split(':',1)[1])
   continue
  m=re.fullmatch(r'(\d+)\s+mod\s+(\d+)',line)
  if not m:raise ValueError('invalid congruence')
  a,n=map(int,m.groups())
  if n<2 or not 0<=a<n:raise ValueError('invalid residue or modulus')
  pairs.append((a,n))
 if not pairs or len({n for a,n in pairs})!=len(pairs):raise ValueError('empty system or duplicate modulus')
 if minimum!=min(n for a,n in pairs):raise ValueError('minimum modulus header differs')
 period=math.lcm(*(n for a,n in pairs))
 if period>cap:raise ValueError('period cap exceeded; coverage not decided')
 covered=bytearray(period)
 for a,n in pairs:
  for x in range(a,period,n):covered[x]=1
 try:witness=covered.index(0)
 except ValueError:return {'covered':True,'period':period}
 raise ValueError(f'uncovered integer: {witness}')
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('file');p.add_argument('--max-period',type=int,default=1000000);a=p.parse_args()
 try:print(check(a.file,a.max_period))
 except (ValueError,OSError)as e:print(e,file=sys.stderr);return 1
 return 0
if __name__=='__main__':sys.exit(main())
