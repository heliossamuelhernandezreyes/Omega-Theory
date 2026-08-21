"""Omega Theory Phase 05 — automorphisms of local continuation structure.
No observational data, fitted parameters, gauge group, or quantum rule.
"""
import itertools
from collections import Counter

def edges(n):
    return [(i,j) for i in range(n) for j in range(n) if i != j]

def graph_from_mask(n,mask):
    E=edges(n); A=[[0]*n for _ in range(n)]
    for k,(i,j) in enumerate(E):
        if (mask>>k)&1: A[i][j]=1
    return A

def automorphisms(A):
    n=len(A)
    return [p for p in itertools.permutations(range(n))
            if all(A[i][j]==A[p[i]][p[j]] for i in range(n) for j in range(n))]

def outgoing_orbits(A,source,autos):
    neigh=[j for j in range(len(A)) if A[source][j]]
    H=[p for p in autos if p[source]==source]
    unseen=set(neigh); out=[]
    while unseen:
        seed=next(iter(unseen)); orb={seed}; changed=True
        while changed:
            changed=False
            for v in tuple(orb):
                for p in H:
                    w=p[v]
                    if w in neigh and w not in orb:
                        orb.add(w); changed=True
        unseen-=orb; out.append(tuple(sorted(orb)))
    return tuple(sorted(out))

if __name__ == "__main__":
    n=4; instances=matches=0; hist=Counter(); group_hist=Counter()
    for mask in range(1 << (n*(n-1))):
        A=graph_from_mask(n,mask); autos=automorphisms(A)
        group_hist[len(autos)] += 1
        for x in range(n):
            if sum(A[x])<2: continue
            instances += 1
            k=len(outgoing_orbits(A,x,autos))
            dP=max(k-1,0); dR=max(k-1,0)
            matches += (dP==dR)
            hist[(k,dP,dR)] += 1
    print("instances",instances)
    print("dimension_matches",matches)
    print("hist",dict(sorted(hist.items())))
    print("graph_automorphism_group_size_hist",dict(sorted(group_hist.items())))
