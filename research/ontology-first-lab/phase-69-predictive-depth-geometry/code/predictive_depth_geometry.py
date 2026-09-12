from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from itertools import product
from math import sqrt
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class GraphSpec:
    name: str
    n: int
    edges: tuple[tuple[int, int], ...]


def cycle(n: int) -> GraphSpec:
    edges = tuple(sorted({tuple(sorted((i, (i + 1) % n))) for i in range(n)}))
    return GraphSpec(f"cycle_{n}", n, edges)


def grid(shape: tuple[int, ...], name: str) -> GraphSpec:
    coords = list(product(*[range(s) for s in shape]))
    idx = {c: i for i, c in enumerate(coords)}
    edges = set()
    for c in coords:
        for a in range(len(shape)):
            if c[a] + 1 < shape[a]:
                d = list(c)
                d[a] += 1
                edges.add(tuple(sorted((idx[c], idx[tuple(d)]))))
    return GraphSpec(name, len(coords), tuple(sorted(edges)))


def binary_tree_depth2() -> GraphSpec:
    # root + 2 children + 4 grandchildren
    edges = ((0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6))
    return GraphSpec("binary_tree_depth2", 7, edges)


def complete(n: int) -> GraphSpec:
    edges = tuple((i, j) for i in range(n) for j in range(i + 1, n))
    return GraphSpec(f"complete_{n}", n, edges)


def specs() -> list[GraphSpec]:
    return [
        cycle(6),
        grid((2, 3), "grid2_2x3"),
        grid((2, 2, 2), "grid3_2x2x2"),
        grid((2, 2, 2, 2), "grid4_hypercube_2^4"),
        binary_tree_depth2(),
        complete(5),
    ]


def adjacency(spec: GraphSpec, active_mask: int | None = None) -> list[list[int]]:
    adj = [[] for _ in range(spec.n)]
    for k, (u, v) in enumerate(spec.edges):
        if active_mask is None or ((active_mask >> k) & 1):
            adj[u].append(v)
            adj[v].append(u)
    return adj


def components(adj: list[list[int]]) -> list[int]:
    n = len(adj)
    out = [0] * n
    seen = [False] * n
    for s in range(n):
        if seen[s]:
            continue
        q = [s]
        seen[s] = True
        comp = []
        while q:
            u = q.pop()
            comp.append(u)
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    q.append(v)
        size = len(comp)
        for u in comp:
            out[u] = size
    return out


def observable(spec: GraphSpec, mask: int) -> tuple[tuple[int, int], ...]:
    adj = adjacency(spec, mask)
    comp_sizes = components(adj)
    return tuple(sorted((len(adj[v]), comp_sizes[v]) for v in range(spec.n)))


def initial_partition(spec: GraphSpec) -> list[int]:
    nstates = 1 << len(spec.edges)
    ids: dict[tuple[tuple[int, int], ...], int] = {}
    part = [0] * nstates
    for x in range(nstates):
        o = observable(spec, x)
        if o not in ids:
            ids[o] = len(ids)
        part[x] = ids[o]
    return part


def refine(spec: GraphSpec, part: list[int]) -> list[int]:
    sig_to_id = {}
    new = [0] * len(part)
    for x in range(len(part)):
        transitions = tuple(part[x ^ (1 << a)] for a in range(len(spec.edges)))
        sig = (part[x], transitions)
        if sig not in sig_to_id:
            sig_to_id[sig] = len(sig_to_id)
        new[x] = sig_to_id[sig]
    return new


def same_partition(a: list[int], b: list[int]) -> bool:
    if len(a) != len(b):
        return False
    mapping_ab = {}
    mapping_ba = {}
    for x, y in zip(a, b):
        if x in mapping_ab and mapping_ab[x] != y:
            return False
        if y in mapping_ba and mapping_ba[y] != x:
            return False
        mapping_ab[x] = y
        mapping_ba[y] = x
    return True


def predictive_depth(spec: GraphSpec) -> tuple[int, int, list[int]]:
    p = initial_partition(spec)
    depth = 0
    while True:
        q = refine(spec, p)
        if same_partition(p, q):
            return depth, len(set(p)), p
        p = q
        depth += 1


def graph_metrics(spec: GraphSpec) -> dict[str, float | int | str]:
    adj = adjacency(spec, None)
    degrees = [len(x) for x in adj]
    mean_degree = sum(degrees) / spec.n
    var = sum((d - mean_degree) ** 2 for d in degrees) / spec.n
    degree_cv = sqrt(var) / mean_degree if mean_degree else 0.0

    dists = []
    balls1 = []
    balls2 = []
    for s in range(spec.n):
        dist = [-1] * spec.n
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        dists.append(max(dist))
        balls1.append(sum(1 for d in dist if 0 <= d <= 1))
        balls2.append(sum(1 for d in dist if 0 <= d <= 2))

    g1_vals = [b2 / b1 for b1, b2 in zip(balls1, balls2) if b1]
    return {
        "name": spec.name,
        "n": spec.n,
        "m": len(spec.edges),
        "mean_degree": mean_degree,
        "degree_cv": degree_cv,
        "diameter": max(dists),
        "mean_B1": sum(balls1) / spec.n,
        "mean_B2": sum(balls2) / spec.n,
        "g1": sum(g1_vals) / len(g1_vals),
    }


def main() -> None:
    outdir = Path(__file__).resolve().parents[1] / "results"
    outdir.mkdir(parents=True, exist_ok=True)

    rows = []
    for spec in specs():
        metrics = graph_metrics(spec)
        nstates = 1 << len(spec.edges)
        depth, nclasses, _ = predictive_depth(spec)
        metrics.update({
            "microstates": nstates,
            "d_star": depth,
            "predictive_classes": nclasses,
        })
        rows.append(metrics)
        print(metrics)

    fields = [
        "name", "n", "m", "microstates", "mean_degree", "degree_cv",
        "diameter", "mean_B1", "mean_B2", "g1", "d_star", "predictive_classes"
    ]
    with (outdir / "summary.tsv").open("w", encoding="utf-8") as f:
        f.write("\t".join(fields) + "\n")
        for r in rows:
            f.write("\t".join(str(r[k]) for k in fields) + "\n")

    pairs = []
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            a, b = rows[i], rows[j]
            if a["d_star"] == b["d_star"]:
                pairs.append((a["name"], b["name"], a["d_star"], a["diameter"], b["diameter"], a["g1"], b["g1"]))

    with (outdir / "counterexamples.tsv").open("w", encoding="utf-8") as f:
        f.write("graph_a\tgraph_b\tshared_d_star\tdiameter_a\tdiameter_b\tg1_a\tg1_b\n")
        for row in pairs:
            f.write("\t".join(str(x) for x in row) + "\n")


if __name__ == "__main__":
    main()
