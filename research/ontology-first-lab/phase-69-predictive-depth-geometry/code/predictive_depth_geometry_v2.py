from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
from math import sqrt
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

def adjacency(spec: GraphSpec, active_mask: int | None = None) -> list[list[int]]:
    adj=[[] for _ in range(spec.n)]
    for k,(u,v) in enumerate(spec.edges):
        if active_mask is None or ((active_mask>>k)&1):
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

def initial_partition(spec: GraphSpec) -> list[int]:
    nstates=1<<len(spec.edges); ids={}; part=[0]*nstates
    for x in range(nstates):
        o=observable(spec,x)
        if o not in ids: ids[o]=len(ids)
        part[x]=ids[o]
    return part

def refine(spec: GraphSpec, part: list[int]) -> list[int]:
    ids={}; new=[0]*len(part)
    for x in range(len(part)):
        sig=(part[x], tuple(part[x^(1<<a)] for a in range(len(spec.edges))))
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

def predictive_depth(spec: GraphSpec) -> tuple[int,int]:
    p=initial_partition(spec); depth=0
    while True:
        q=refine(spec,p)
        if same_partition(p,q): return depth, len(set(p))
        p=q; depth+=1

def graph_metrics(spec: GraphSpec) -> dict:
    adj=adjacency(spec,None); deg=[len(x) for x in adj]
    mean=sum(deg)/spec.n; var=sum((d-mean)**2 for d in deg)/spec.n
    cv=sqrt(var)/mean if mean else 0.0
    ecc=[]; b1=[]; b2=[]
    for s in range(spec.n):
        dist=[-1]*spec.n; dist[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if dist[v]==-1: dist[v]=dist[u]+1; q.append(v)
        ecc.append(max(dist)); b1.append(sum(d<=1 for d in dist)); b2.append(sum(d<=2 for d in dist))
    return {"name":spec.name,"n":spec.n,"m":len(spec.edges),"mean_degree":mean,"degree_cv":cv,
            "diameter":max(ecc),"mean_B1":sum(b1)/spec.n,"mean_B2":sum(b2)/spec.n,
            "g1":sum(y/x for x,y in zip(b1,b2))/spec.n}

def main() -> None:
    outdir=Path(__file__).resolve().parents[1]/"results"; outdir.mkdir(parents=True, exist_ok=True)
    rows=[]
    for spec in specs():
        r=graph_metrics(spec); states=1<<len(spec.edges); r["microstates"]=states
        if states>MAX_EXACT_MICROSTATES:
            r.update(status="NO_EJECUTADA_EXACT_LIMIT", d_star="", predictive_classes="")
        else:
            d,c=predictive_depth(spec); r.update(status="EXACT", d_star=d, predictive_classes=c)
        rows.append(r); print(r)
    fields=["name","n","m","microstates","status","mean_degree","degree_cv","diameter","mean_B1","mean_B2","g1","d_star","predictive_classes"]
    with (outdir/"summary.tsv").open("w",encoding="utf-8") as f:
        f.write("\t".join(fields)+"\n")
        for r in rows: f.write("\t".join(str(r[k]) for k in fields)+"\n")
    exact=[r for r in rows if r["status"]=="EXACT"]
    with (outdir/"counterexamples.tsv").open("w",encoding="utf-8") as f:
        f.write("graph_a\tgraph_b\tshared_d_star\tdiameter_a\tdiameter_b\tg1_a\tg1_b\n")
        for i,a in enumerate(exact):
            for b in exact[i+1:]:
                if a["d_star"]==b["d_star"]:
                    f.write(f'{a["name"]}\t{b["name"]}\t{a["d_star"]}\t{a["diameter"]}\t{b["diameter"]}\t{a["g1"]}\t{b["g1"]}\n')

if __name__=="__main__": main()
