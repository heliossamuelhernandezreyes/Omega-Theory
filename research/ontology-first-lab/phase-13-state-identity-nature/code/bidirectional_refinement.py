"""
Omega Theory Phase 13 — state, identity, nature separation.

Exhaustive tests on all 4096 directed graphs on four labelled nodes without
self-loops, plus all 5^5 deterministic functional systems on five states.

No probabilities, fitted parameters, physical labels, or observational data.
"""
import itertools
from collections import Counter, defaultdict

def edges(n):
    return [(i,j) for i in range(n) for j in range(n) if i != j]

def graph_from_mask(n, mask, E):
    A = [[0]*n for _ in range(n)]
    for k,(i,j) in enumerate(E):
        A[i][j] = (mask >> k) & 1
    return A

def canon_part(groups):
    return tuple(sorted(tuple(sorted(g)) for g in groups))

def block_map(part):
    return {x:i for i,b in enumerate(part) for x in b}

def refine(A, mode):
    n = len(A)
    part = (tuple(range(n)),)
    steps = 0
    while True:
        b = block_map(part)
        new = []
        for block in part:
            groups = defaultdict(set)
            for x in block:
                fut = tuple(sorted({b[y] for y in range(n) if A[x][y]}))
                past = tuple(sorted({b[y] for y in range(n) if A[y][x]}))
                sig = fut if mode == "future" else past if mode == "past" else (past, fut)
                groups[sig].add(x)
            new.extend(groups.values())
        nxt = canon_part(new)
        if nxt == part:
            return part, steps
        part = nxt
        steps += 1

def scc_partition(A):
    n = len(A)
    seen = [False]*n
    order = []
    def dfs(v):
        seen[v] = True
        for w in range(n):
            if A[v][w] and not seen[w]:
                dfs(w)
        order.append(v)
    for v in range(n):
        if not seen[v]:
            dfs(v)
    R = [[A[j][i] for j in range(n)] for i in range(n)]
    seen = [False]*n
    comps = []
    def dfs2(v,c):
        seen[v] = True
        c.add(v)
        for w in range(n):
            if R[v][w] and not seen[w]:
                dfs2(w,c)
    for v in reversed(order):
        if not seen[v]:
            c=set(); dfs2(v,c); comps.append(c)
    return canon_part(comps)

def automorphisms(A):
    n = len(A)
    return [p for p in itertools.permutations(range(n))
            if all(A[i][j] == A[p[i]][p[j]]
                   for i in range(n) for j in range(n))]

def aut_partition(A):
    autos = automorphisms(A)
    n = len(A)
    unseen = set(range(n))
    groups = []
    while unseen:
        seed = next(iter(unseen))
        orb = {p[seed] for p in autos}
        changed = True
        while changed:
            changed = False
            for v in list(orb):
                for p in autos:
                    if p[v] not in orb:
                        orb.add(p[v]); changed = True
        unseen -= orb
        groups.append(orb)
    return canon_part(groups)

def refines(P,Q):
    qmap = block_map(Q)
    return all(len({qmap[x] for x in b}) == 1 for b in P)

if __name__ == "__main__":
    n=4; E=edges(n); N=1 << len(E)
    future_equals_past=joint_refines_future=joint_refines_past=0
    joint_equals_scc=joint_equals_aut=joint_discrete=0
    block_hists={m:Counter() for m in ("future","past","joint","scc","aut")}
    for mask in range(N):
        A=graph_from_mask(n,mask,E)
        pf,_=refine(A,"future"); pp,_=refine(A,"past"); pj,_=refine(A,"joint")
        ps=scc_partition(A); pa=aut_partition(A)
        future_equals_past += (pf == pp)
        joint_refines_future += refines(pj,pf)
        joint_refines_past += refines(pj,pp)
        joint_equals_scc += (pj == ps)
        joint_equals_aut += (pj == pa)
        joint_discrete += (len(pj) == n)
        for name,p in (("future",pf),("past",pp),("joint",pj),("scc",ps),("aut",pa)):
            block_hists[name][len(p)] += 1
    print("n4 graphs",N)
    print("future_equals_past",future_equals_past)
    print("joint_refines_future",joint_refines_future)
    print("joint_refines_past",joint_refines_past)
    print("joint_equals_scc",joint_equals_scc)
    print("joint_equals_aut",joint_equals_aut)
    print("joint_discrete",joint_discrete)
    print("block_hists",block_hists)

    n=5; total=n**n
    hist={m:Counter() for m in ("future","past","joint")}
    joint_more=0
    for f in itertools.product(range(n), repeat=n):
        A=[[0]*n for _ in range(n)]
        for i,j in enumerate(f): A[i][j]=1
        pf,_=refine(A,"future"); pp,_=refine(A,"past"); pj,_=refine(A,"joint")
        for name,p in (("future",pf),("past",pp),("joint",pj)):
            hist[name][len(p)] += 1
        joint_more += (len(pj) > len(pf))
    print("n5 functional systems",total)
    print("joint_more_informative_than_future",joint_more)
    print("functional_hists",hist)
