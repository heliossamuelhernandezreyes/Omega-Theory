from collections import defaultdict


def canon(parts):
    return tuple(sorted(tuple(sorted(b)) for b in parts))


def bmap(P):
    return {x: i for i, block in enumerate(P) for x in block}


def compute(nA):
    """Exact Moore minimization for A with nA nodes plus one external B."""
    n = nA + 1
    B = nA
    A_edges = [(i, j) for i in range(nA) for j in range(nA) if i != j]
    Dint = len(A_edges)
    Dcross = nA
    Ng = 1 << Dint
    Nx = 1 << Dcross
    N = Ng * Nx
    colors = [0] * nA + [1]

    internal_outs = []
    for g in range(Ng):
        outs = [0] * n
        for k, (i, j) in enumerate(A_edges):
            if (g >> k) & 1:
                outs[i] |= 1 << j
        internal_outs.append(outs)

    def pi_star_from_outs(outs):
        P = canon((tuple(range(nA)), (B,)))
        while True:
            bm = bmap(P)
            groups = []
            for block in P:
                buckets = {}
                for x in block:
                    sigset = 0
                    om = outs[x]
                    for y in range(n):
                        if (om >> y) & 1:
                            sigset |= 1 << bm[y]
                    sig = (colors[x], sigset)
                    buckets.setdefault(sig, []).append(x)
                groups.extend(tuple(v) for v in buckets.values())
            Q = canon(groups)
            if Q == P:
                return Q
            P = Q

    outputs = [None] * N
    for g in range(Ng):
        baseouts = internal_outs[g]
        for xmask in range(Nx):
            outs = baseouts.copy()
            for i in range(nA):
                if (xmask >> i) & 1:
                    outs[i] |= 1 << B
            outputs[g * Nx + xmask] = pi_star_from_outs(outs)

    output_ids = {}
    outc = [0] * N
    for s, o in enumerate(outputs):
        if o not in output_ids:
            output_ids[o] = len(output_ids)
        outc[s] = output_ids[o]

    def refine(cls):
        ids = {}
        new = [0] * N
        for g in range(Ng):
            base = g * Nx
            for x in range(Nx):
                s = base + x
                sig = (outc[s],) + tuple(
                    cls[base + (x ^ (1 << e))] for e in range(Dcross)
                )
                if sig not in ids:
                    ids[sig] = len(ids)
                new[s] = ids[sig]
        return new, len(ids)

    cls = outc[:]
    all_history = [len(set(cls))]
    depth = 0
    while True:
        new, count = refine(cls)
        all_history.append(count)
        depth += 1
        if new == cls:
            cls = new
            break
        cls = new

    initial = [g * Nx for g in range(Ng)]
    full_initial = len({cls[s] for s in initial})

    cls_d = outc[:]
    initial_history = [len({cls_d[s] for s in initial})]
    dstar = 0 if initial_history[-1] == full_initial else None
    for d in range(1, depth + 1):
        cls_d, _ = refine(cls_d)
        count = len({cls_d[s] for s in initial})
        initial_history.append(count)
        if dstar is None and count == full_initial:
            dstar = d

    return {
        "nA": nA,
        "internal_edges": Dint,
        "internal_microstates": Ng,
        "cross_masks": Nx,
        "total_interaction_states": N,
        "current_output_classes_initial": initial_history[0],
        "first_order_classes_initial": initial_history[1] if len(initial_history) > 1 else initial_history[0],
        "full_predictive_classes_initial": full_initial,
        "d_star_initial": dstar,
        "all_state_class_history": all_history,
        "initial_class_history": initial_history,
    }


if __name__ == "__main__":
    for nA in (1, 2, 3, 4):
        print(compute(nA))
