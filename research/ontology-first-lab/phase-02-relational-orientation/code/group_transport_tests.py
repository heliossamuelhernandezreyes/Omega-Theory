"""Omega Theory Phase 02 — finite transport tests.
No U(1), complex amplitudes, Born rule, observational constants or fitting.
"""
from itertools import product, permutations

GROUPS = {
    "Z2": [[0,1],[1,0]],
    "Z3": [[0,1,2],[1,2,0],[2,0,1]],
    "Z4": [[0,1,2,3],[1,2,3,0],[2,3,0,1],[3,0,1,2]],
    "V4": [[0,1,2,3],[1,0,3,2],[2,3,0,1],[3,2,1,0]],
}
S3=list(permutations(range(3)))
idx={p:i for i,p in enumerate(S3)}
def compose(p,q): return tuple(p[q[i]] for i in range(3))
GROUPS["S3"]=[[idx[compose(p,q)] for q in S3] for p in S3]

def inv_table(T):
    n=len(T)
    return [next(j for j in range(n) if T[i][j]==0 and T[j][i]==0) for i in range(n)]

def mul(T,*xs):
    r=0
    for x in xs: r=T[r][x]
    return r

def conjugate(T,g,h):
    inv=inv_table(T)
    return mul(T,g,h,inv[g])

def transform(T,edges,gauges):
    inv=inv_table(T); a,b,c=edges; g0,g1,g2=gauges
    return (mul(T,g0,a,inv[g1]),mul(T,g1,b,inv[g2]),mul(T,g2,c,inv[g0]))

if __name__ == "__main__":
    print("group order abelian distinct_h tests exact invariant_by_conjugacy")
    for name,T in GROUPS.items():
        n=len(T); total=exact=cov=0; hs=set()
        for edges in product(range(n),repeat=3):
            h=mul(T,*edges); hs.add(h)
            for gauges in product(range(n),repeat=3):
                total+=1
                h2=mul(T,*transform(T,edges,gauges))
                exact += (h2==h)
                cov += (h2==conjugate(T,gauges[0],h))
        abelian=all(T[i][j]==T[j][i] for i in range(n) for j in range(n))
        print(name,n,abelian,len(hs),total,exact,cov)
