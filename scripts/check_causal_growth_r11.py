#!/usr/bin/env python3
"""Omega R11: causal-order-only transitive percolation, an ALREADY KNOWN model.

No geometry, Hilbert space, seconds, Hamiltonian, matter or energy is assumed.
A parameter p is an explicit EXTRA dynamical law: it is NOT derived from Gamma.
Enumeration uses natural birth labels for bookkeeping, then compares isomorphism
classes of transitive closures; labels are NOT physical birth times.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path


def pair_indices(n: int) -> tuple[tuple[int, int], ...]:
    if not 1 <= n <= 6:
        raise ValueError('1 <= n <= 6 required for exact enumeration')
    return tuple((i,j) for i in range(n) for j in range(i+1,n))


def closure(n: int, relations: list[tuple[int,int]] | tuple[tuple[int,int], ...]):
    """Transitive closure of strict DAG; arbitrary distinct integer labels accepted."""
    r = [[False]*n for _ in range(n)]
    for i,j in relations:
        if i == j or not (0 <= i < n and 0 <= j < n):
            raise ValueError('no reflexive or out-of-range relations')
        r[i][j]=True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]: r[i][j] = True
    if any(r[i][i] for i in range(n)):
        raise ValueError('cyclic causal relation')
    return tuple(tuple(row) for row in r)


def covers(r):
    """Intrinsic Hasse diagram: ignore shortcut edges implied by transitivity."""
    n=len(r)
    return tuple((i,j) for i in range(n) for j in range(n)
                 if r[i][j] and not any(r[i][k] and r[k][j]
                                            for k in range(n)))


def relabel(r, order):
    """order[new_index] = old_index: passive coordinate change."""
    return tuple(tuple(r[order[i]][order[j]] for j in range(len(r)))
                 for i in range(len(r)))


def canonical(r):
    """Finite n<=5 unlabeled causal poset invariant under arbitrary permutations."""
    n=len(r)
    if n>5: raise ValueError('canonical exhaustive only up to 5')
    return min(tuple(int(r[perm[i]][perm[j]]) for i in range(n)
                     for j in range(n)) for perm in itertools.permutations(range(n)))


def height(r):
    """Number of events along longest causal chain; ordinal, NOT proper time."""
    n=len(r)
    cache={}
    def length(i):
        if i not in cache:
            cache[i]=1+max((length(j) for j in range(n) if r[i][j]),default=0)
        return cache[i]
    return max((length(i) for i in range(n)),default=0)


def classify_three(r):
    if len(r)!=3: raise ValueError('requires 3 events')
    edges=sum(sum(row) for row in r)
    if edges==0:return 'antichain'
    if edges==1:return 'single_relation'
    if edges==3:return 'chain'
    if edges!=2:raise ValueError('invalid poset of 3')
    max_count=sum(not any(r[i][j] for j in range(3)) for i in range(3))
    return 'vee' if max_count==1 else 'lambda'


def exact_distribution(n, p):
    """Distribution over UNLABELED finite causets by summing natural-label paths.

    Every allowed pair i<j has a primitive attempted edge with probability p,
    independently; directed transitive closure supplies all implied relations.
    """
    if not(1<=n<=5 and 0<p<1 and math.isfinite(p)):
        raise ValueError('1<=n<=5, 0<p<1 finite')
    pairs=pair_indices(n)
    result=defaultdict(float)
    hist=defaultdict(float)
    representative={}
    for bits in itertools.product((0,1), repeat=len(pairs)):
        edges=[ij for ij,b in zip(pairs,bits) if b]
        prob=p**sum(bits)*(1-p)**(len(bits)-sum(bits))
        r=closure(n,edges)
        key=canonical(r)
        result[key]+=prob
        hist[height(r)]+=prob
        representative[key]=r
    return dict(result),dict(hist),representative


def exact_three_closed_form(p):
    return {'antichain':(1-p)**3,
            'single_relation':3*p*(1-p)**2,
            'vee':p*p*(1-p),
            'lambda':p*p*(1-p),
            'chain':p*p}


def experiment():
    cases=[]
    for p in (.2,.5,.8):
        d,h,reps=exact_distribution(3,p)
        classes={classify_three(reps[key]):weight for key,weight in d.items()}
        assert len(classes)==5
        analytic=exact_three_closed_form(p)
        assert all(math.isclose(classes[c],analytic[c],abs_tol=1e-12) for c in analytic)
        assert math.isclose(sum(classes.values()),1,abs_tol=1e-12)
        mean=sum(k*v for k,v in h.items())
        assert math.isclose(mean,2-(1-p)**3+p**2,abs_tol=1e-12)
        cases.append({'p_assumed':p,'distribution':dict(sorted(classes.items())),
                      'mean_ordinal_height':mean,
                      'expected_height_closed_form':'2 - (1-p)^3 + p^2',
                      'history_n_events':3})
    # Invariance of causal relations under redundant edge representation
    short=closure(3,[(0,1),(1,2)])
    long=closure(3,[(0,1),(1,2),(0,2)])
    assert short==long and covers(short)==covers(long)
    # Arbitrary relabeling of an already formed causal order
    v=closure(4,[(0,1),(1,2),(0,3)])
    assert canonical(v)==canonical(relabel(v,(3,1,0,2)))
    # Counting possible support never determines p in open (0,1)
    assert all(x['distribution']['chain']>0 for x in cases)
    return {'status':'PASS only for a known, explicitly parameterized classical toy law',
            'question':'Does causal compatibility and label-invariance select rates?',
            'answer':'NO: one parameter family shares same support, different observables',
            'model':'transitive percolation (Rideout-Sorkin precursor), NOT new to Omega',
            'n3_analytic_formula':exact_three_closed_form(.5),
            'cases':cases,
            'invariants':{'cover_graph_ignores_redundant_edges':True,
                          'causal_order_isomorphic_under_relabel':True,
                          'no_global_physical_duration_assigned':True,
                          'all_five_three_event_types_positive_for_0<p<1':True},
            'limitations':['p must be INPUT: no law selecting dynamics from Gamma_x',
                           'birth labels are representation, not physical external clock',
                           'number of births and causal height are ordinal, not seconds',
                           'percolation is classical probability, no quantum interference',
                           'label-invariance of final observables is weaker than full relativistic general covariance',
                           'causal poset does not derive measured volume scale, c, hbar, gauge fields, gravity',
                           'not a uniqueness, Lorentz-recovery or physical validation claim']}


def save(folder):
    folder.mkdir(parents=True,exist_ok=True)
    result=experiment()
    (folder/'OMEGA_R11_CAUSAL_GROWTH_RESULTS.json').write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (folder/'OMEGA_R11_CAUSAL_GROWTH_CASES.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow(['p_assumed','p_antichain','p_one_relation','p_vee','p_lambda','p_chain','mean_ordinal_height'])
        for row in result['cases']:
            d=row['distribution']
            writer.writerow([row['p_assumed'],d['antichain'],d['single_relation'],
                             d['vee'],d['lambda'],d['chain'],row['mean_ordinal_height']])


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',type=Path)
    args=ap.parse_args()
    if args.out is not None:save(args.out)
    print(json.dumps(experiment(),ensure_ascii=False,indent=2))
