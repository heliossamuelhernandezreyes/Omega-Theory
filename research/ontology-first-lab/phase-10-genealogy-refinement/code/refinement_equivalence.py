"""Omega Theory Phase 10 — refinement equivalence candidate.

Given a partition pi of micro-configurations, map a genealogy to macro labels and
collapse consecutive repetitions. Two genealogies are refinement-equivalent iff
their collapsed macro traces coincide.

Exhaustive domain: all 15 set partitions of four microstates and all sequences
up to three transitions.
"""
import itertools


def set_partitions(items):
    items=list(items)
    if not items:
        yield []
        return
    first=items[0]
    for rest in set_partitions(items[1:]):
        yield [{first}] + [set(b) for b in rest]
        for i in range(len(rest)):
            new=[set(b) for b in rest]
            new[i].add(first)
            yield new


def canonical(part):
    return tuple(sorted(tuple(sorted(b)) for b in part))


def block_map(part):
    return {x:i for i,b in enumerate(part) for x in b}


def macro_trace(path, block):
    out=[]
    for x in path:
        z=block[x]
        if not out or out[-1] != z:
            out.append(z)
    return tuple(out)


if __name__ == '__main__':
    nodes=tuple(range(4))
    parts=sorted(set(canonical(p) for p in set_partitions(nodes)))
    paths=[]
    for L in range(1,5):
        paths.extend(itertools.product(nodes, repeat=L))

    signatures=set()
    insertion_ok=True
    for part in parts:
        b=block_map(part)
        signatures.add(tuple(macro_trace(p,b) for p in paths))
        for p in paths:
            if len(p)>=4:
                continue
            for i,x in enumerate(p):
                for y in nodes:
                    if b[y]==b[x]:
                        refined=p[:i+1]+(y,)+p[i+1:]
                        insertion_ok &= macro_trace(refined,b)==macro_trace(p,b)

    print('partitions',len(parts))
    print('distinct_refinement_relations',len(signatures))
    print('same_block_insertion_invariance',insertion_ok)
