"""Phase 11: exhaustive parameter-free stable coarse-graining test for n=4."""
import itertools

def edges(n): return [(i,j) for i in range(n) for j in range(n) if i!=j]
def graph(n,m):
    A=[[0]*n for _ in range(n)]; E=edges(n)
    for k,(i,j) in enumerate(E): A[i][j]=(m>>k)&1
    return A

def parts(items):
    items=list(items)
    if not items: yield []; return
    x=items[0]
    for rest in parts(items[1:]):
        yield [{x}]+[set(b) for b in rest]
        for i in range(len(rest)):
            z=[set(b) for b in rest]; z[i].add(x); yield z

def canon(p): return tuple(sorted(tuple(sorted(b)) for b in p))
def stable(A,p):
    bm={x:i for i,b in enumerate(p) for x in b}
    for b in p:
        sig=[]
        for x in b:
            sig.append(tuple(sorted({bm[y] for y in range(len(A)) if A[x][y]})))
        if len(set(sig))>1: return False
    return True

if __name__=='__main__':
    n=4; P=sorted(set(canon(p) for p in parts(range(n))))
    total=0; unique=0; multi=0
    for m in range(1<<(n*(n-1))):
        A=graph(n,m); S=[p for p in P if stable(A,p)]; total+=len(S)
        k=min(map(len,S)); C=[p for p in S if len(p)==k]
        unique += (len(C)==1)
        multi += (sum(1 for p in S if 1<len(p)<n)>1)
    print('graphs',1<<(n*(n-1)))
    print('total_stable_partitions',total)
    print('unique_coarsest',unique)
    print('multiple_nontrivial',multi)
