import itertools
import math
from collections import Counter, defaultdict


def edges(n):
    return [(i, j) for i in range(n) for j in range(n) if i != j]


def graph_edges_from_mask(n, m):
    E = edges(n)
    return {(i, j) for k, (i, j) in enumerate(E) if (m >> k) & 1}


def aut_size(n, m):
    G = graph_edges_from_mask(n, m)
    return sum(
        1
        for p in itertools.permutations(range(n))
        if {(p[i], p[j]) for i, j in G} == G
    )


def canon(parts):
    return tuple(sorted(tuple(sorted(b)) for b in parts))


def bmap(P):
    return {x: i for i, b in enumerate(P) for x in b}


def pi_star(n, m):
    G = graph_edges_from_mask(n, m)
    P = (tuple(range(n)),)
    outs = defaultdict(set)
    for i, j in G:
        outs[i].add(j)
    while True:
        bm = bmap(P)
        groups = []
        for B in P:
            buckets = defaultdict(list)
            for x in B:
                sig = tuple(sorted({bm[y] for y in outs[x]}))
                buckets[sig].append(x)
            groups.extend(buckets.values())
        Q = canon(groups)
        if Q == P:
            return P
        P = Q


def build_histories():
    n = 3
    E = edges(n)
    D = len(E)
    aut = [aut_size(n, m) for m in range(1 << D)]
    pis = [pi_star(n, m) for m in range(1 << D)]
    hist = []

    for depth in (2, 3, 4, 5):
        for toggles in itertools.product(range(D), repeat=depth):
            states = [0]
            m = 0
            for e in toggles:
                m ^= 1 << e
                states.append(m)
            tv = sum(
                abs(math.log(aut[states[i + 1]]) - math.log(aut[states[i]]))
                for i in range(depth)
            )
            pi_trace = []
            for s in states:
                p = pis[s]
                if not pi_trace or p != pi_trace[-1]:
                    pi_trace.append(p)
            hist.append(
                dict(
                    depth=depth,
                    toggles=toggles,
                    endpoint=m,
                    W=depth,
                    TV=round(tv, 12),
                    PiTrace=tuple(pi_trace),
                    last_edge=toggles[-1],
                    edge_hist=tuple(Counter(toggles)[i] for i in range(D)),
                )
            )
    return hist, D


def test_sufficiency():
    hist, D = build_histories()

    compressions = {
        "Gamma": lambda h: (h["endpoint"],),
        "Gamma_W": lambda h: (h["endpoint"], h["W"]),
        "Gamma_W_TV": lambda h: (h["endpoint"], h["W"], h["TV"]),
        "Gamma_W_TV_PiTrace": lambda h: (
            h["endpoint"], h["W"], h["TV"], h["PiTrace"]
        ),
        "Gamma_edge_hist": lambda h: (h["endpoint"], h["edge_hist"]),
        "full_history": lambda h: h["toggles"],
    }

    rules = {
        "endpoint_only": lambda h: h["endpoint"] % D,
        "W_dependent": lambda h: (h["endpoint"] + h["W"]) % D,
        "TV_dependent": lambda h: (
            h["endpoint"] + int(round(h["TV"] * 1_000_000))
        ) % D,
        "PiTrace_dependent": lambda h: (
            h["endpoint"] + len(h["PiTrace"])
        ) % D,
        "last_edge_dependent": lambda h: (
            h["endpoint"] + h["last_edge"]
        ) % D,
        "edge_hist_dependent": lambda h: (
            h["endpoint"]
            + sum((i + 1) * c for i, c in enumerate(h["edge_hist"]))
        ) % D,
        "full_order_dependent": lambda h: hash(h["toggles"]) % D,
    }

    results = []
    for rname, rule in rules.items():
        for cname, comp in compressions.items():
            groups = defaultdict(set)
            for h in hist:
                groups[comp(h)].add(rule(h))
            ambiguous = sum(1 for vals in groups.values() if len(vals) > 1)
            results.append(
                (rname, cname, len(groups), ambiguous, ambiguous == 0)
            )
    return results


if __name__ == "__main__":
    for row in test_sufficiency():
        print(row)
