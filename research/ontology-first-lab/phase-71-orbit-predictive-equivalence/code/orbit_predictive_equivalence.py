from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations
from pathlib import Path

@dataclass(frozen=True)
class GraphSpec:
    n: int
    edges: tuple[tuple[int, int], ...]
    canonical: str


def all_possible_edges(n: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(n), 2))


def edge_set_from_mask(n: int, mask: int) -> tuple[tuple[int, int], ...]:
    poss = all_possible_edges(n)
    return tuple(poss[i] for i in range(len(poss)) if (mask >> i) & 1)


def connected(n: int, edges: tuple[tuple[int, int], ...]) -> bool:
    if n == 0:
        return False
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def graph_bitstring(n: int, edges: tuple[tuple[int, int], ...]) -> str:
    eset = set(edges)
    return "".join("1" if e in eset else "0" for e in all_possible_edges(n))


def permute_edges(edges: tuple[tuple[int, int], ...], p: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple(sorted(tuple(sorted((p[u], p[v]))) for u, v in edges))


def canonical_form(n: int, edges: tuple[tuple[int, int], ...]) -> str:
    return min(graph_bitstring(n, permute_edges(edges, p)) for p in permutations(range(n)))


def connected_unlabeled_graphs(n: int) -> list[GraphSpec]:
    poss = all_possible_edges(n)
    reps: dict[str, tuple[tuple[int, int], ...]] = {}
    for mask in range(1 << len(poss)):
        edges = tuple(poss[i] for i in range(len(poss)) if (mask >> i) & 1)
        if not connected(n, edges):
            continue
        key = canonical_form(n, edges)
        if key not in reps:
            reps[key] = edges
    return [GraphSpec(n, tuple(sorted(reps[k])), k) for k in sorted(reps)]


def automorphisms(spec: GraphSpec) -> list[tuple[int, ...]]:
    eset = set(spec.edges)
    out = []
    for p in permutations(range(spec.n)):
        if set(permute_edges(spec.edges, p)) == eset:
            out.append(p)
    return out


def edge_orbits(spec: GraphSpec, autos: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    edge_index = {e: i for i, e in enumerate(spec.edges)}
    remaining = set(range(len(spec.edges)))
    out = []
    while remaining:
        seed = min(remaining)
        u, v = spec.edges[seed]
        orb = set()
        for p in autos:
            e = tuple(sorted((p[u], p[v])))
            orb.add(edge_index[e])
        out.append(tuple(sorted(orb)))
        remaining -= orb
    return sorted(out, key=lambda o: (len(o), o))


def active_adjacency(spec: GraphSpec, mask: int) -> list[list[int]]:
    adj = [[] for _ in range(spec.n)]
    for i, (u, v) in enumerate(spec.edges):
        if (mask >> i) & 1:
            adj[u].append(v)
            adj[v].append(u)
    return adj


def component_sizes(adj: list[list[int]]) -> list[int]:
    n = len(adj)
    out = [0] * n
    seen = [False] * n
    for s in range(n):
        if seen[s]:
            continue
        comp = []
        stack = [s]
        seen[s] = True
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
        for u in comp:
            out[u] = len(comp)
    return out


def observable(spec: GraphSpec, mask: int) -> tuple[tuple[int, int], ...]:
    adj = active_adjacency(spec, mask)
    cs = component_sizes(adj)
    return tuple(sorted((len(adj[v]), cs[v]) for v in range(spec.n)))


def initial_partition(spec: GraphSpec) -> list[int]:
    ids = {}
    part = []
    for x in range(1 << len(spec.edges)):
        o = observable(spec, x)
        if o not in ids:
            ids[o] = len(ids)
        part.append(ids[o])
    return part


def refine_relational(part: list[int], orbits: list[tuple[int, ...]]) -> list[int]:
    ids = {}
    new = [0] * len(part)
    for x in range(len(part)):
        responses = []
        for orb in orbits:
            responses.append(tuple(sorted({part[x ^ (1 << a)] for a in orb})))
        sig = (part[x], tuple(responses))
        if sig not in ids:
            ids[sig] = len(ids)
        new[x] = ids[sig]
    return new


def same_partition(a: list[int], b: list[int]) -> bool:
    ab, ba = {}, {}
    for x, y in zip(a, b):
        if x in ab and ab[x] != y:
            return False
        if y in ba and ba[y] != x:
            return False
        ab[x] = y
        ba[y] = x
    return True


def predictive_partition(spec: GraphSpec, orbits: list[tuple[int, ...]]) -> tuple[list[int], int, list[int]]:
    p = initial_partition(spec)
    counts = [len(set(p))]
    depth = 0
    while True:
        q = refine_relational(p, orbits)
        if same_partition(p, q):
            return p, depth, counts
        p = q
        depth += 1
        counts.append(len(set(p)))


def transform_mask(spec: GraphSpec, mask: int, p: tuple[int, ...]) -> int:
    edge_index = {e: i for i, e in enumerate(spec.edges)}
    out = 0
    for i, (u, v) in enumerate(spec.edges):
        if (mask >> i) & 1:
            e = tuple(sorted((p[u], p[v])))
            out |= 1 << edge_index[e]
    return out


def orbit_partition(spec: GraphSpec, autos: list[tuple[int, ...]]) -> list[int]:
    ids = {}
    out = []
    for x in range(1 << len(spec.edges)):
        key = min(transform_mask(spec, x, p) for p in autos)
        if key not in ids:
            ids[key] = len(ids)
        out.append(ids[key])
    return out


def partition_failure(a: list[int], b: list[int]) -> tuple[str, int, int] | None:
    n = len(a)
    for x in range(n):
        for y in range(x + 1, n):
            same_a = a[x] == a[y]
            same_b = b[x] == b[y]
            if same_a != same_b:
                if same_a and not same_b:
                    return "predictive_merges_distinct_aut_orbits", x, y
                return "predictive_splits_aut_orbit", x, y
    return None


def main() -> None:
    outdir = Path(__file__).resolve().parents[1] / "results"
    outdir.mkdir(parents=True, exist_ok=True)
    rows = []
    failures = []
    for n in range(2, 6):
        specs = connected_unlabeled_graphs(n)
        for spec in specs:
            autos = automorphisms(spec)
            eorbs = edge_orbits(spec, autos)
            p_pred, depth, counts = predictive_partition(spec, eorbs)
            p_orb = orbit_partition(spec, autos)
            failure = partition_failure(p_pred, p_orb)
            equal = failure is None
            row = dict(
                n=n,
                m=len(spec.edges),
                canonical=spec.canonical,
                aut_size=len(autos),
                edge_orbits=len(eorbs),
                edge_orbit_sizes=",".join(map(str, map(len, eorbs))),
                microstates=1 << len(spec.edges),
                observable_classes=len(set(initial_partition(spec))),
                aut_orbit_classes=len(set(p_orb)),
                predictive_classes=len(set(p_pred)),
                d_star_rel=depth,
                refinement_counts="->".join(map(str, counts)),
                equal_partitions=str(equal),
                failure_type="" if equal else failure[0],
            )
            rows.append(row)
            if failure is not None:
                failures.append((n, len(spec.edges), spec.canonical, failure[1], failure[2], failure[0], spec, p_pred, p_orb))
    fields = ["n","m","canonical","aut_size","edge_orbits","edge_orbit_sizes","microstates","observable_classes","aut_orbit_classes","predictive_classes","d_star_rel","refinement_counts","equal_partitions","failure_type"]
    with (outdir / "summary.tsv").open("w", encoding="utf-8") as f:
        f.write("\t".join(fields) + "\n")
        for r in rows:
            f.write("\t".join(str(r[k]) for k in fields) + "\n")
    with (outdir / "counterexample.tsv").open("w", encoding="utf-8") as f:
        f.write("n\tm\tcanonical\tx\ty\tfailure_type\tpredictive_class_x\tpredictive_class_y\taut_orbit_x\taut_orbit_y\n")
        if failures:
            failures.sort(key=lambda z: (z[0], z[1], z[2], z[3], z[4]))
            n, m, canon, x, y, ft, spec, pp, po = failures[0]
            f.write(f"{n}\t{m}\t{canon}\t{x}\t{y}\t{ft}\t{pp[x]}\t{pp[y]}\t{po[x]}\t{po[y]}\n")
    counts_by_n = {}
    for r in rows:
        counts_by_n[r["n"]] = counts_by_n.get(r["n"], 0) + 1
    print("connected_unlabeled_counts", counts_by_n)
    print("graphs_tested", len(rows))
    print("failures", len(failures))
    if failures:
        f0 = sorted(failures, key=lambda z: (z[0], z[1], z[2], z[3], z[4]))[0]
        print("minimal_counterexample", f0[:6])
    else:
        print("minimal_counterexample", None)

if __name__ == "__main__":
    main()
