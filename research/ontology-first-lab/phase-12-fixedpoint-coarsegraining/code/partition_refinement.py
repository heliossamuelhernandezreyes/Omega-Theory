"""Omega Theory Phase 12 — iterative structural partition refinement.

Start from one block containing all configurations. At each iteration split every
block according to the SET of current macro-blocks reachable in one update.
Repeat until no split occurs. No probabilities, weights, geometry or observed data.

The research report records a critical limitation: this set-valued criterion
collapses every 5-state functional transition system tested to one block.
"""
from collections import defaultdict

def block_map(part):
    return {x:i for i,b in enumerate(part) for x in b}

def canonical(blocks):
    return tuple(sorted(tuple(sorted(b)) for b in blocks))

def signature(A, part, x):
    b = block_map(part)
    return tuple(sorted({b[y] for y in range(len(A)) if A[x][y]}))

def refine_once(A, part):
    new=[]
    for block in part:
        groups=defaultdict(set)
        for x in block:
            groups[signature(A,part,x)].add(x)
        new.extend(groups.values())
    return canonical(new)

def fixedpoint(A):
    part=(tuple(range(len(A))),)
    while True:
        nxt=refine_once(A,part)
        if nxt==part:
            return part
        part=nxt
