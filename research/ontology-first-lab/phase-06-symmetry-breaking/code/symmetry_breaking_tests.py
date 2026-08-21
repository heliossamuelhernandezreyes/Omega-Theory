"""Omega Theory Phase 06 — structural symmetry breaking.
Exhaustive n=4 directed graphs; fixed outgoing channel sets.
"""
import itertools
from collections import Counter

def edges(n):
    return [(i,j) for i in range(n) for j in range(n) if i != j]

def graph_from_mask(n,mask):
    E=edges(n); A=[[0]*n for _ in range(n)]
    for k,(i,j) in enumerate(E): A[i][j]=(mask>>k)&1
    return A

def automorphisms(A):
    n=len(A)
    return [p for p in itertools.permutations(range(n)) if all(A[i][j]==A[p[i]][p[j]] for i in range(n) for j in range(n))]

def stabilizer(autos,x):
    return [p for p in autos if p[x]==x]

def outgoing(A,x):
    return tuple(j for j in range(len(A)) if A[x][j])

def orbits_on_set(S,H):
    unseen=set(S); orbs=[]
    while unseen:
        seed=next(iter(unseen)); orb={seed}; changed=True
        while changed:
            changed=False
            for v in tuple(orb):
                for p in H:
                    w=p[v]
                    if w in S and w not in orb:
                        orb.add(w); changed=True
        unseen-=orb; orbs.append(tuple(sorted(orb)))
    return tuple(sorted(orbs))

def local_data(A,x):
    autos=automorphisms(A); H=stabilizer(autos,x); S=outgoing(A,x)
    orbs=orbits_on_set(S,H); d=len(S); k=len(orbs)
    return len(H), d, k, max(k-1,0), max(d-k,0)

if __name__=="__main__":
    n=4; E=edges(n); counts=Counter(); delta=Counter(); tested=0
    for mask in range(1<<(n*(n-1))):
        A=graph_from_mask(n,mask)
        for x in range(n):
            if sum(A[x])<2: continue
            b=local_data(A,x)
            for ei,(u,v) in enumerate(E):
                if u==x: continue
                m2=mask^(1<<ei)
                if mask>=m2: continue
                a=local_data(graph_from_mask(n,m2),x)
                assert b[1]==a[1]
                tested+=1
                dk=a[2]-b[2]
                cls="orbit_split" if dk>0 else "orbit_merge" if dk<0 else "orbit_unchanged"
                counts[cls]+=1
                delta[(dk,a[0]-b[0],a[4]-b[4])]+=1
    print("tested",tested)
    print("transition_counts",dict(counts))
    print("delta_hist",dict(sorted(delta.items())))
