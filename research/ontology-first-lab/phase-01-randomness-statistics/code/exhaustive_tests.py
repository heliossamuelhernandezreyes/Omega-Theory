"""Omega Theory Phase 01: exhaustive structural tests.

No fitted parameters, observational constants, random sampling, Born rule,
or assumed complex amplitudes.
"""
import itertools


def edges(n):
    return [(i, j) for i in range(n) for j in range(n) if i != j]


def graph(n, mask):
    es = edges(n)
    return [[int(i != j and ((mask >> es.index((i, j))) & 1)) if i != j else 0
             for j in range(n)] for i in range(n)]


def automorphisms(a):
    n = len(a)
    return [p for p in itertools.permutations(range(n))
            if all(a[i][j] == a[p[i]][p[j]] for i in range(n) for j in range(n))]


def outgoing_orbits(a, source, autos):
    neigh = [j for j in range(len(a)) if a[source][j]]
    fix = [p for p in autos if p[source] == source]
    unseen = set(neigh)
    result = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {seed}
        changed = True
        while changed:
            changed = False
            for v in tuple(orbit):
                for p in fix:
                    w = p[v]
                    if w in neigh and w not in orbit:
                        orbit.add(w)
                        changed = True
        unseen -= orbit
        result.append(orbit)
    return result


def partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first = items[0]
    for rest in partitions(items[1:]):
        yield [{first}] + [set(b) for b in rest]
        for i in range(len(rest)):
            new = [set(b) for b in rest]
            new[i].add(first)
            yield new


def canonical_partition(part):
    return tuple(sorted(tuple(sorted(b)) for b in part))


def symmetry_test(n=4):
    branching = unique = 0
    free_hist = {}
    for mask in range(1 << (n * (n - 1))):
        a = graph(n, mask)
        autos = automorphisms(a)
        for source in range(n):
            degree = sum(a[source])
            if degree < 2:
                continue
            branching += 1
            orbit_count = len(outgoing_orbits(a, source, autos))
            free = orbit_count - 1
            free_hist[free] = free_hist.get(free, 0) + 1
            unique += int(orbit_count == 1)
    return branching, unique, free_hist


def coarse_graining_test(n=4):
    parts = sorted(set(canonical_partition(p) for p in partitions(range(n))))
    totals = {2: [0, 0], 3: [0, 0]}
    for f in itertools.product(range(n), repeat=n):
        for part in parts:
            m = len(part)
            if m not in totals:
                continue
            block = {x: bi for bi, b in enumerate(part) for x in b}
            branching = any(len({block[f[x]] for x in b}) > 1 for b in part)
            totals[m][0] += 1
            totals[m][1] += int(branching)
    return totals


if __name__ == "__main__":
    branching, unique, hist = symmetry_test()
    print("branching_node_instances", branching)
    print("uniquely_fixed_by_symmetry", unique)
    print("uniquely_fixed_fraction", unique / branching)
    print("free_parameter_histogram", hist)
    for m, (total, apparent) in coarse_graining_test().items():
        print(f"coarse_graining_{m}_macroblocks", apparent, total, apparent / total)
