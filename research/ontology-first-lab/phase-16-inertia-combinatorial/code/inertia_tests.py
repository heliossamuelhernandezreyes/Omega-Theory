"""Omega Theory Phase 16 — combinatorial precursor of relational inertia.

Exhaustive on all 4096 directed graphs with 4 labeled nodes, no self-loops,
and all 15 set partitions. No probabilities, rates, energies or fitted parameters.
"""
from collections import Counter, deque

INF = 10**9

def edges(n): return [(i,j) for i in range(n) for j in range(n) if i != j]

def graph_from_mask(n, mask, E):
    A=[[0]*n for _ in range(n)]
    for k,(i,j) in enumerate(E): A[i][j]=(mask>>k)&1
    return A

def partitions(items):
    items=list(items)
    if not items:
        yield []; return
    first=items[0]
    for rest in partitions(items[1:]):
        yield [{first}] + [set(b) for b in rest]
        for i in range(len(rest)):
            new=[set(b) for b in rest]; new[i].add(first); yield new

def canon(part): return tuple(sorted(tuple(sorted(b)) for b in part))
def block_map(part): return {x:i for i,b in enumerate(part) for x in b}

def stable(A, part):
    bm=block_map(part); n=len(A)
    for block in part:
        sigs=[tuple(sorted({bm[y] for y in range(n) if A[x][y]})) for x in block]
        if len(set(sigs))>1: return False
    return True

def exit_distance(A, part, x):
    bm=block_map(part); b0=bm[x]; n=len(A)
    q=deque([(x,0)]); seen={x}
    while q:
        v,d=q.popleft()
        for w in range(n):
            if not A[v][w]: continue
            if bm[w] != b0: return d+1
            if w not in seen:
                seen.add(w); q.append((w,d+1))
    return INF

def refines(P,Q):
    qm=block_map(Q)
    return all(len({qm[x] for x in block})==1 for block in P)

if __name__ == '__main__':
    n=4; E=edges(n)
    parts=sorted(set(canon(p) for p in partitions(range(n))))
    all_dist=Counter(); stable_dist=Counter(); stable_pairs=0
    rep_tests=rep_ok=mono_tests=mono_ok=equal=strict=0
    for mask in range(1 << len(E)):
        A=graph_from_mask(n,mask,E)
        stable_parts=[p for p in parts if stable(A,p)]
        stable_pairs += len(stable_parts)
        for p in parts:
            for x in range(n):
                d=exit_distance(A,p,x); all_dist['inf' if d==INF else d]+=1
            if p in stable_parts:
                for x in range(n):
                    d=exit_distance(A,p,x); stable_dist['inf' if d==INF else d]+=1
                for block in p:
                    rep_tests+=1; rep_ok += len({exit_distance(A,p,x) for x in block})==1
        for fine in stable_parts:
            for coarse in stable_parts:
                if fine==coarse or not refines(fine,coarse): continue
                for x in range(n):
                    df=exit_distance(A,fine,x); dc=exit_distance(A,coarse,x)
                    mono_tests+=1; mono_ok += (dc==INF) or (df!=INF and dc>=df)
                    if dc==df: equal+=1
                    else: strict+=1
    print('stable_pairs', stable_pairs)
    print('all_dist', dict(all_dist))
    print('stable_dist', dict(stable_dist))
    print('representative_invariance', rep_ok, '/', rep_tests)
    print('refinement_monotonicity', mono_ok, '/', mono_tests)
    print('equal', equal, 'strict', strict)
