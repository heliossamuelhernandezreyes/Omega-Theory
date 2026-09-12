from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path

MAX_EXACT_MICROSTATES = 1_000_000

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
                d = list(c); d[a] += 1
                edges.add(tuple(sorted((idx[c], idx[tuple(d)]))))
    return GraphSpec(name, len(coords), tuple(sorted(edges)))

def binary_tree_depth2() -> GraphSpec:
    return GraphSpec("binary_tree_depth2", 7, ((0,1),(0,2),(1,3),(1,4),(2,5),(2,6)))

def complete(n: int) -> GraphSpec:
    return GraphSpec(f"complete_{n}", n, tuple((i,j) for i in range(n) for j in range(i+1,n)))

def specs() -> list[GraphSpec]:
    return [
        cycle(6),
        grid((2,3), "grid2_2x3"),
        grid((2,2,2), "grid3_2x2x2"),
        grid((2,2,2,2), "grid4_hypercube_2^4"),
        binary_tree_depth2(),
        complete(5),
    ]

def adjacency(spec: GraphSpec, mask: int | None = None) -> list[list[int]]:
    adj=[[] for _ in range(spec.n)]
    for k,(u,v) in enumerate(spec.edges):
        if mask is None or ((mask>>k)&1):
            adj[u].append(v); adj[v].append(u)
    return adj

def components(adj: list[list[int]]) -> list[int]:
    n=len(adj); out=[0]*n; seen=[False]*n
    for s in range(n):
        if seen[s]: continue
        stack=[s]; seen[s]=True; comp=[]
        while stack:
            u=stack.pop(); comp.append(u)
            for v in adj[u]:
                if not seen[v]: seen[v]=True; stack.append(v)
        for u in comp: out[u]=len(comp)
    return out

def observable(spec: GraphSpec, mask: int) -> tuple[tuple[int,int], ...]:
    adj=adjacency(spec, mask); cs=components(adj)
    return tuple(sorted((len(adj[v]), cs[v]) for v in range(spec.n)))

def automorphisms(spec: GraphSpec) -> list[tuple[int,...]]:
    eset=set(spec.edges)
    autos=[]
    for p in permutations(range(spec.n)):
        mapped={tuple(sorted((p[u],p[v]))) for u,v in spec.edges}
        if mapped==eset:
            autos.append(p)
    return autos

def edge_orbits(spec: GraphSpec, autos: list[tuple[int,...]]) -> list[tuple[int,...]]:
    edge_index={e:i for i,e in enumerate(spec.edges)}
    remaining=set(range(len(spec.edges))); out=[]
    while remaining:
        seed=min(remaining); u,v=spec.edges[seed]
        orb=set()
        for p in autos:
            e=tuple(sorted((p[u],p[v])))
            orb.add(edge_index[e])
        out.append(tuple(sorted(orb))); remaining-=orb
    return sorted(out, key=lambda o:(len(o),o))

def initial_partition(spec: GraphSpec) -> list[int]:
    nstates=1<<len(spec.edges); ids={}; part=[0]*nstates
    for x in range(nstates):
        o=observable(spec,x)
        if o not in ids: ids[o]=len(ids)
        part[x]=ids[o]
    return part

def refine_relational(spec: GraphSpec, part: list[int], orbits: list[tuple[int,...]]) -> list[int]:
    ids={}; new=[0]*len(part)
    for x in range(len(part)):
        responses=[]
        for orb in orbits:
            response=tuple(sorted({part[x^(1<<a)] for a in orb}))
            responses.append(response)
        sig=(part[x], tuple(responses))
        if sig not in ids: ids[sig]=len(ids)
        new[x]=ids[sig]
    return new

def same_partition(a: list[int], b: list[int]) -> bool:
    ab={}; ba={}
    for x,y in zip(a,b):
        if x in ab and ab[x]!=y: return False
        if y in ba and ba[y]!=x: return False
        ab[x]=y; ba[y]=x
    return True

def predictive_depth_rel(spec: GraphSpec, orbits: list[tuple[int,...]]) -> tuple[int,int,list[int]]:
    p=initial_partition(spec); counts=[len(set(p))]; depth=0
    while True:
        q=refine_relational(spec,p,orbits)
        if same_partition(p,q): return depth,len(set(p)),counts
        p=q; depth+=1; counts.append(len(set(p)))

def transform_mask(spec: GraphSpec, mask: int, p: tuple[int,...]) -> int:
    edge_index={e:i for i,e in enumerate(spec.edges)}; out=0
    for i,(u,v) in enumerate(spec.edges):
        if (mask>>i)&1:
            e=tuple(sorted((p[u],p[v]))); out |= 1<<edge_index[e]
    return out

def microstate_orbit_count(spec: GraphSpec, autos: list[tuple[int,...]]) -> int:
    nstates=1<<len(spec.edges); seen=set(); count=0
    for x in range(nstates):
        if x in seen: continue
        orb={transform_mask(spec,x,p) for p in autos}
        seen.update(orb); count+=1
    return count

def main() -> None:
    outdir=Path(__file__).resolve().parents[1]/"results"; outdir.mkdir(parents=True, exist_ok=True)
    rows=[]
    for spec in specs():
        states=1<<len(spec.edges)
        if states>MAX_EXACT_MICROSTATES:
            rows.append(dict(name=spec.name,n=spec.n,m=len(spec.edges),microstates=states,status="NO_EJECUTADA_EXACT_LIMIT",aut_size="",edge_orbits="",edge_orbit_sizes="",observable_classes="",microstate_aut_orbits="",d_star_rel="",predictive_classes="",refinement_counts="")); continue
        autos=automorphisms(spec); orbs=edge_orbits(spec,autos)
        p0=initial_partition(spec)
        d,c,counts=predictive_depth_rel(spec,orbs)
        rows.append(dict(name=spec.name,n=spec.n,m=len(spec.edges),microstates=states,status="EXACT",aut_size=len(autos),edge_orbits=len(orbs),edge_orbit_sizes=",".join(map(str,map(len,orbs))),observable_classes=len(set(p0)),microstate_aut_orbits=microstate_orbit_count(spec,autos),d_star_rel=d,predictive_classes=c,refinement_counts="->".join(map(str,counts))))
        print(rows[-1])
    fields=["name","n","m","microstates","status","aut_size","edge_orbits","edge_orbit_sizes","observable_classes","microstate_aut_orbits","d_star_rel","predictive_classes","refinement_counts"]
    with (outdir/"summary.tsv").open("w",encoding="utf-8") as f:
        f.write("\t".join(fields)+"\n")
        for r in rows: f.write("\t".join(str(r[k]) for k in fields)+"\n")
    exact=[r for r in rows if r["status"]=="EXACT"]
    with (outdir/"counterexamples.tsv").open("w",encoding="utf-8") as f:
        f.write("graph_a\tgraph_b\tshared_d_star_rel\tedge_orbits_a\tedge_orbits_b\tpredictive_classes_a\tpredictive_classes_b\n")
        for i,a in enumerate(exact):
            for b in exact[i+1:]:
                if a["d_star_rel"]==b["d_star_rel"]:
                    f.write(f'{a["name"]}\t{b["name"]}\t{a["d_star_rel"]}\t{a["edge_orbits"]}\t{b["edge_orbits"]}\t{a["predictive_classes"]}\t{b["predictive_classes"]}\n')

if __name__=="__main__": main()
