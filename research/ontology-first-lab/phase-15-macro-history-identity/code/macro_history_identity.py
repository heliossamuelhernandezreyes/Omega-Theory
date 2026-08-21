"""Omega Theory Phase 15 — macro identity as history equivalence.

Enumerates all 4096 directed graphs on 4 labelled nodes without self-loops,
all 15 set partitions, and compatible histories to depth 3.
No probabilities, observed data, energy or physical labels.
"""
import itertools
from collections import defaultdict, Counter

def edges(n): return [(i,j) for i in range(n) for j in range(n) if i!=j]

def graph(n,mask,E):
    A=[[0]*n for _ in range(n)]
    for k,(i,j) in enumerate(E): A[i][j]=(mask>>k)&1
    return A

def partitions(items):
    items=list(items)
    if not items:
        yield []; return
    a=items[0]
    for rest in partitions(items[1:]):
        yield [{a}]+[set(b) for b in rest]
        for i in range(len(rest)):
            new=[set(b) for b in rest]; new[i].add(a); yield new

def canon(p): return tuple(sorted(tuple(sorted(b)) for b in p))
def bmap(p): return {x:i for i,b in enumerate(p) for x in b}

def stable(A,p):
    m=bmap(p); n=len(A)
    for block in p:
        sigs=[tuple(sorted({m[y] for y in range(n) if A[x][y]})) for x in block]
        if len(set(sigs))>1: return False
    return True

def histories(A,D):
    H={(i,) for i in range(len(A))}; front=set(H)
    for _ in range(D):
        nxt=set()
        for h in front:
            for y in range(len(A)):
                if A[h[-1]][y]: nxt.add(h+(y,))
        H|=nxt; front=nxt
    return H

def trace(h,m):
    out=[]
    for x in h:
        z=m[x]
        if not out or out[-1]!=z: out.append(z)
    return tuple(out)

if __name__=='__main__':
    n=4; D=3; E=edges(n)
    P=sorted(set(canon(p) for p in partitions(range(n))))
    M=Counter(); B=Counter()
    for mask in range(1<<len(E)):
        A=graph(n,mask,E); H=histories(A,D)
        for p in P:
            m=bmap(p); st=stable(A,p)
            G=defaultdict(list)
            for h in H: G[trace(h,m)].append(h)
            M['micro_histories']+=len(H); M['macro_identity_classes']+=len(G)
            M['extra_microhistories_collapsed']+=sum(max(0,len(v)-1) for v in G.values())
            for h in H:
                if len(h)-1>=D: continue
                t=trace(h,m)
                for y in range(n):
                    if not A[h[-1]][y]: continue
                    hp=h+(y,); tp=trace(hp,m)
                    if m[y]==m[h[-1]]:
                        M['internal_tests']+=1; M['internal_ok']+=(tp==t)
                    else:
                        M['external_tests']+=1; M['external_ok']+=(len(tp)==len(t)+1 and tp[:-1]==t)
            for t,members in G.items():
                sets=[]
                for h in members:
                    if len(h)-1>=D: continue
                    sets.append({trace(h+(y,),m) for y in range(n) if A[h[-1]][y]})
                if sets and st:
                    M['rep_tests']+=1; M['rep_ok']+=(len({frozenset(s) for s in sets})==1)
                if sets:
                    strict={u for s in sets for u in s if u!=t}; B[len(strict)]+=1
    print(M); print(B)
