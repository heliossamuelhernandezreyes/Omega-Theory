"""Omega Theory Phase 17 — structural support of macro-accessibility changes.

Exhaustive on all 4096 directed graphs with 4 labeled nodes, no self-loops,
and all 15 set partitions. Support is an edit count, not physical energy.
"""
from collections import Counter


def edges(n):
    return [(i,j) for i in range(n) for j in range(n) if i != j]


def graph_from_mask(n, mask, E):
    A=[[0]*n for _ in range(n)]
    for k,(i,j) in enumerate(E):
        A[i][j]=(mask>>k)&1
    return A


def partitions(items):
    items=list(items)
    if not items:
        yield []
        return
    first=items[0]
    for rest in partitions(items[1:]):
        yield [{first}] + [set(b) for b in rest]
        for i in range(len(rest)):
            new=[set(b) for b in rest]
            new[i].add(first)
            yield new


def canon(part):
    return tuple(sorted(tuple(sorted(b)) for b in part))


def block_map(part):
    return {x:i for i,b in enumerate(part) for x in b}


def stable(A, part):
    bm=block_map(part); n=len(A)
    for block in part:
        sigs=[]
        for x in block:
            sigs.append(tuple(sorted({bm[y] for y in range(n) if A[x][y]})))
        if len(set(sigs)) > 1:
            return False
    return True


def macro_targets(A, part, block_index):
    bm=block_map(part)
    x=part[block_index][0]
    return {bm[y] for y in range(len(A)) if A[x][y]}


def open_support(A, part, source_index, target_index):
    B=part[source_index]; C=part[target_index]
    return sum(not any(A[x][y] for y in C) for x in B)


def close_support(A, part, source_index, target_index):
    B=part[source_index]; C=part[target_index]
    return sum(A[x][y] for x in B for y in C)


if __name__ == '__main__':
    n=4; E=edges(n)
    parts=sorted(set(canon(p) for p in partitions(range(n))))
    stable_pairs=0
    open_hist=Counter(); close_hist=Counter(); closed_hist=Counter()
    open_tests=open_eq=0
    close_tests=close_lb=0

    for mask in range(1 << len(E)):
        A=graph_from_mask(n,mask,E)
        for p in parts:
            if not stable(A,p):
                continue
            stable_pairs += 1
            k=len(p)
            for bi,B in enumerate(p):
                targets=macro_targets(A,p,bi)
                absent=[ci for ci in range(k) if ci != bi and ci not in targets]
                for ci in absent:
                    s=open_support(A,p,bi,ci)
                    open_hist[s]+=1; open_tests+=1
                    open_eq += (s == len(B))
                external={ci for ci in targets if ci != bi}
                if not external and k>1:
                    vals=[open_support(A,p,bi,ci) for ci in range(k) if ci != bi]
                    if vals:
                        closed_hist[min(vals)] += 1
                for ci in external:
                    s=close_support(A,p,bi,ci)
                    close_hist[s]+=1; close_tests+=1
                    close_lb += (s >= len(B))

    print('stable_pairs',stable_pairs)
    print('open_hist',dict(sorted(open_hist.items())))
    print('open_equals_block_size',open_eq,'/',open_tests)
    print('closed_block_open_hist',dict(sorted(closed_hist.items())))
    print('close_hist',dict(sorted(close_hist.items())))
    print('close_ge_block_size',close_lb,'/',close_tests)
