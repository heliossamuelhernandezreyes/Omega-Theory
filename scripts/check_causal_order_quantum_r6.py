#!/usr/bin/env python3
"""Omega R6 - partial-order quantum gates without a preferred GLOBAL schedule.

Toy finite qubit causal graph with strictly local unitary events. Choosing linear
extensions for evaluation is bookkeeping and NOT a physical universal clock.
The qubits, allowed gates, their angles, and local event precedence are inputs.
NO emergence of physical time, Lorentz symmetry, c, hbar, or Omega ontology.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import cos, sin, sqrt
from random import Random
from collections import defaultdict
import cmath, json, argparse
from pathlib import Path

N_QUBITS = 7
DIM = 1 << N_QUBITS

@dataclass(frozen=True)
class Event:
    name: str
    support: tuple[int, ...]
    kind: str
    theta: float = 0.0
    def __post_init__(self):
        assert len(self.support) in (1,2), self
        assert len(set(self.support)) == len(self.support)
        assert all(0 <= s < N_QUBITS for s in self.support)
        assert self.kind in ('RY','H','Z','X','CNOT')
        assert (self.kind == 'CNOT') == (len(self.support)==2)


def events():
    """Three causal branches: spatial influence chain + independent A/B clocks.

    'Join' is a local two-qubit interaction after both clock worldlines;
    earlier events on different supports remain unordered.
    """
    spatial = [Event('P0',(0,), 'X')] + [Event('L%d%d'%(i,i+1),(i,i+1),'CNOT') for i in range(4)]
    clock_a = [Event('A%d'%i,(5,), 'RY',0.35) for i in range(1,5)]
    clock_b = [Event('B%d'%i,(6,), 'RY',0.22) for i in range(1,7)]
    return spatial+clock_a+clock_b+[Event('J',(5,6),'CNOT')]


def dependency_graph(es):
    """Worldline order: each event depends on the latest prior use of each site.

    The list specifies *local* sequence per site. There is no imposed ordering
    between disjoint support events, hence a genuine partial order.
    """
    latest = {}
    parents = {}
    for e in es:
        if e.name in parents:
            raise ValueError('duplicate event name')
        parents[e.name] = set(latest[q] for q in e.support if q in latest)
        for q in e.support: latest[q] = e.name
    return parents


def topo_order(es, seed=None, preference=None):
    rng=Random(seed)
    deps=dependency_graph(es)
    by_name={e.name:e for e in es}
    done=set(); output=[]
    while len(done)<len(es):
        ready=[e for e in es if e.name not in done and deps[e.name].issubset(done)]
        if not ready: raise ValueError('cycle')
        if preference=='A':
            ready.sort(key=lambda e: (0 if e.name.startswith('A') else 1,e.name))
            chosen=ready[0]
        elif preference=='B':
            ready.sort(key=lambda e: (0 if e.name.startswith('B') else 1,e.name))
            chosen=ready[0]
        else:
            chosen=rng.choice(ready)
        output.append(chosen)
        done.add(chosen.name)
    return output


def ket_zero():
    return [1+0j]+[0j]*(DIM-1)


def gate(state, e):
    """Apply strictly local gate, with qubits indexed by bit positions."""
    out=state.copy()
    if e.kind=='CNOT':
        c,t=e.support
        for k in range(DIM):
            if (k>>c)&1 and not (k>>t)&1:
                k2=k^(1<<t)
                out[k],out[k2]=state[k2],state[k]
        return out
    q=e.support[0]
    if e.kind=='X':
        for k in range(DIM):
            if not (k>>q)&1:
                k2=k^(1<<q); out[k],out[k2]=state[k2],state[k]
    elif e.kind=='Z':
        for k in range(DIM):
            if (k>>q)&1: out[k]=-state[k]
    else:
        if e.kind=='RY':
            a,b,d,f=cos(e.theta/2),-sin(e.theta/2),sin(e.theta/2),cos(e.theta/2)
        else:  # H
            a,b,d,f=1/sqrt(2),1/sqrt(2),1/sqrt(2),-1/sqrt(2)
        for k in range(DIM):
            if not (k>>q)&1:
                k2=k^(1<<q)
                out[k]=a*state[k]+b*state[k2]
                out[k2]=d*state[k]+f*state[k2]
    return out


def state_after(seq, initial=None):
    psi=ket_zero() if initial is None else initial
    for e in seq: psi=gate(psi,e)
    return psi


def probability_one(psi, q):
    return sum(abs(a)**2 for k,a in enumerate(psi) if (k>>q)&1)


def norm2(psi): return sum(abs(a)**2 for a in psi)


def max_error(a,b): return max(abs(x-y) for x,y in zip(a,b))


def prefix_counts(sequence, n=8):
    first=sequence[:n]
    return dict(A=sum(e.name.startswith('A') for e in first),
                B=sum(e.name.startswith('B') for e in first),
                propagation=sum(e.name.startswith('L') or e.name=='P0' for e in first))


def causal_front():
    """One preparation at q0 plus nearest-neighbor CNOT bridges.

    Compare control X|0> vs no preparation. After bridge s, targets at
    distance > s stay at the SAME one-site state; nearer ones differ.
    """
    psi0=ket_zero()
    psi1=gate(ket_zero(),Event('injection',(0,),'X'))
    cases=[]
    for bridges in range(5):
        if bridges:
            e=Event('bridge',(bridges-1,bridges),'CNOT')
            psi0=gate(psi0,e);psi1=gate(psi1,e)
        delta=[probability_one(psi1,q)-probability_one(psi0,q) for q in range(5)]
        assert all(abs(delta[q])<1e-14 for q in range(bridges+1,5))
        assert all(abs(delta[q]-1)<1e-14 for q in range(bridges+1))
        cases.append({'bridge_events':bridges,'sites_affected':bridges+1,
                      'signal_outside_local_causal_front':0.0,
                      'receiver_q4_change':delta[4]})
    return cases


def noncommuting_counterexample():
    a=Event('H',(0,),'H');b=Event('Z',(0,),'Z')
    ab=state_after([a,b]);ba=state_after([b,a])
    return {'same_support_unordered':True,
            'max_statevector_difference':max_error(ab,ba),
            'overlap_magnitude':abs(sum(x.conjugate()*y for x,y in zip(ab,ba))),
            'distinguishable_X_expectation':1.0}


def microevent_refinement_counterexample():
    e=Event('whole',(5,),'RY',0.8)
    f=Event('half1',(5,),'RY',0.4)
    g=Event('half2',(5,),'RY',0.4)
    one=state_after([e]);two=state_after([f,g])
    return {'max_statevector_difference':max_error(one,two),
            'event_counts_for_same_operational_rotation':[1,2],
            'p_one':probability_one(one,5),'p_two':probability_one(two,5)}


def run(seed=20261017,n_schedules=128):
    es=events(); p=dependency_graph(es)
    assert len(es)==16
    assert p['J']=={'A4','B6'}
    alpha=topo_order(es,preference='A')
    beta=topo_order(es,preference='B')
    state_a=state_after(alpha);state_b=state_after(beta)
    baseline=state_a
    discrepancies=[]
    for j in range(n_schedules):
        order=topo_order(es,seed=seed+j)
        computed=state_after(order)
        discrepancies.append(max_error(baseline,computed))
        assert abs(norm2(computed)-1)<1e-12
    assert max(discrepancies)<1e-12
    assert max_error(state_a,state_b)<1e-12
    clock1=probability_one(state_a,5)
    clock2=probability_one(state_a,6)
    assert abs(clock1-math_sin_sq(4*0.35/2))<1e-12
    # B after a CNOT join is entangled with A; use pre-join B state for local marker
    before_join=state_after([e for e in alpha if e.name!='J'])
    prejoin_b=probability_one(before_join,6)
    assert abs(prejoin_b-math_sin_sq(6*0.22/2))<1e-12
    prefix_a=prefix_counts(alpha)
    prefix_b=prefix_counts(beta)
    assert prefix_a!=prefix_b
    front=causal_front()
    assert front[-1]['receiver_q4_change']==1
    no=noncommuting_counterexample()
    assert no['overlap_magnitude']<1e-14
    ref=microevent_refinement_counterexample()
    assert ref['max_statevector_difference']<1e-14
    return {
      'status':'PASS: CONDITIONAL causal circuit; no physical emergence of time or Omega confirmation',
      'model':'Finite 7-qubit DAG with local RY, X and CNOT events; same local order, variable incomparable event schedules',
      'qubits':N_QUBITS,'events':len(es),'independent_schedules_tested':n_schedules+2,
      'dependency_edges':sum(len(v) for v in p.values()),
      'maximum_state_difference_over_schedules':max(max(discrepancies),max_error(state_a,state_b)),
      'representative_linear_extensions':{
        'A_first':[e.name for e in alpha], 'B_first':[e.name for e in beta]},
      'arbitrary_schedule_prefix_8':{'A_first':prefix_a,'B_first':prefix_b},
      'internal_clock_markers':{'clock_A_rotation_per_event':.35,'clock_B_rotation_per_event':.22,
             'clock_A_events':4,'clock_B_events':6,
             'A_p_excited_at_join':clock1,
             'B_p_excited_before_join':prejoin_b,
             'B_p_excited_after_join':clock2},
      'causal_front_tests':front,
      'unordered_overlap_counterexample':no,
      'refinement_event_count_ambiguity':ref,
      'negative_results':[
        'The DAG is a SPECIFIED quantum circuit, not derived from bare Gamma_x or Omega ontology',
        'No global PHYSICAL step was used, but the evaluator selects an arbitrary topological order',
        'A logical causal partial order is assumed; it is NOT physical proper time or a Lorentz-invariant metric',
        'An event prefix of length eight is NOT an invariant equal-time slice; A/B counts differ across schedules',
        'Unordered overlapping noncommuting gates make predictions ambiguous unless an extra causal edge or rule exists',
        'The angles .35 and .22, number of events and event identity are arbitrary input: no fundamental relative clock rate derived',
        'Refining one rotation into two leaves final state the same but doubles the event count: no physical clock from bare counting',
        'The finite, labeled line graph assumes spatial locality; a cone counted in links cannot set measured c',
        'No gravity, antimatter dynamics, QFT, Lorentz invariance or ħ derived',
      ]}


def math_sin_sq(x): return sin(x)**2


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--schedules',type=int,default=128)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    r=run(n_schedules=args.schedules)
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(r,indent=2,ensure_ascii=False))
