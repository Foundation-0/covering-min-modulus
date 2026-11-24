"""Compare canonical congruences; agreement is not a coverage proof."""
import pathlib,re,json,argparse,hashlib

def read(path):
    headers={};pairs=[];pages=[]
    for number,line in enumerate(pathlib.Path(path).read_text().splitlines(),1):
        line=line.strip()
        if not line:continue
        if line.startswith('#'):
            if ':' in line:
                k,v=line[1:].split(':',1);headers[k.strip()]=v.strip()
            if re.match(r'#\s*page\b',line,re.I):pages.append(dict(line=number,reference=line[1:].strip()))
            continue
        m=re.fullmatch(r'(\d+)\s+mod\s+(\d+)',line)
        if not m:raise ValueError(f'line {number}: invalid congruence')
        a,n=map(int,m.groups())
        if n<2 or not 0<=a<n:raise ValueError('noncanonical congruence')
        pairs.append((a,n))
    if not pairs or len({n for a,n in pairs})!=len(pairs):raise ValueError('empty system or repeated modulus')
    for k in ('source','link','pages','transcribed by','minimum modulus'):
        if not headers.get(k):raise ValueError('missing header '+k)
    if int(headers['minimum modulus'])!=min(n for a,n in pairs):raise ValueError('minimum header mismatch')
    return headers,set(pairs),pages

def compare(left,right):
    lh,l,lp=read(left);rh,r,rp=read(right)
    return dict(agree=l==r,count_left=len(l),count_right=len(r),left_only=sorted(l-r),right_only=sorted(r-l),left_header=lh,right_header=rh,left_page_markers=lp,right_page_markers=rp,left_sha256=hashlib.sha256(pathlib.Path(left).read_bytes()).hexdigest(),right_sha256=hashlib.sha256(pathlib.Path(right).read_bytes()).hexdigest())
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('left');p.add_argument('right');a=p.parse_args();result=compare(a.left,a.right);print(json.dumps(result,indent=2));raise SystemExit(0 if result['agree'] else 1)
