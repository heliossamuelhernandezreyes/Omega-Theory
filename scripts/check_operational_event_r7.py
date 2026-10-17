#!/usr/bin/env python3
"""Omega R7: operational equivalence of qubit events and representation no-go.

Standard-library only. Known quantum-channel and instrument mathematics are
IMPORTED, not derived from Omega ontology. No absolute event/time unit derived.
"""
from __future__ import annotations
import cmath
import json
import math
from typing import Sequence

Matrix = tuple[tuple[complex, ...], ...]

def mat(rows: Sequence[Sequence[complex]]) -> Matrix:
    out = tuple(tuple(complex(x) for x in row) for row in rows)
    if not out or any(len(row) != len(out[0]) for row in out):
        raise ValueError('Matrix must be nonempty and rectangular')
    return out

def add(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError('Shape mismatch')
    return mat([[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)])

def mul(a: Matrix, b: Matrix) -> Matrix:
    if len(a[0]) != len(b):
        raise ValueError('Shape mismatch')
    return mat([[sum(a[i][k]*b[k][j] for k in range(len(b)))
                 for j in range(len(b[0]))] for i in range(len(a))])

def scale(s: complex, a: Matrix) -> Matrix:
    return mat([[s*x for x in row] for row in a])

def dagger(a: Matrix) -> Matrix:
    return mat([[a[i][j].conjugate() for i in range(len(a))] for j in range(len(a[0]))])

def maxdiff(a: Matrix,b: Matrix) -> float:
    if len(a)!=len(b) or len(a[0])!=len(b[0]):
        raise ValueError('Shape mismatch')
    return max(abs(x-y) for ra,rb in zip(a,b) for x,y in zip(ra,rb))

def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(len(a)))

def outer_state(zero: complex, one: complex) -> Matrix:
    v=(complex(zero),complex(one))
    if not math.isclose(sum(abs(x)**2 for x in v),1.,abs_tol=1e-13):
        raise ValueError('Pure state must be normalized')
    return mat([[v[i]*v[j].conjugate() for j in range(2)] for i in range(2)])

I = mat([[1,0],[0,1]])
Z = mat([[1,0],[0,-1]])
P0 = mat([[1,0],[0,0]])
P1 = mat([[0,0],[0,1]])
ZERO = outer_state(1,0)
PLUS = outer_state(1/math.sqrt(2),1/math.sqrt(2))

def ry(angle: float) -> Matrix:
    if not math.isfinite(angle): raise ValueError('Finite angles')
    c,s=math.cos(angle/2),math.sin(angle/2)
    return mat([[c,-s],[s,c]])

def rz(angle: float) -> Matrix:
    if not math.isfinite(angle): raise ValueError('Finite angles')
    return mat([[cmath.exp(-.5j*angle),0],[0,cmath.exp(.5j*angle)]])

def quantum_channel(kraus: Sequence[Matrix], state: Matrix) -> Matrix:
    if not kraus or len(state)!=2 or len(state[0])!=2:
        raise ValueError('Qubit Kraus list and 2x2 operator needed')
    out=mat([[0,0],[0,0]])
    for k in kraus:
        if len(k)!=2 or len(k[0])!=2:
            raise ValueError('2x2 Kraus required')
        out=add(out,mul(mul(k,state),dagger(k)))
    return out

def choi(kraus: Sequence[Matrix]) -> Matrix:
    """Unnormalized 4x4 Choi, J=sum_ij |i><j| ⊗ E(|i><j|)."""
    data=[[0j]*4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            base=mat([[1 if a==i and b==j else 0 for b in range(2)]
                      for a in range(2)])
            output=quantum_channel(kraus,base)
            for a in range(2):
                for b in range(2):
                    data[2*i+a][2*j+b]=output[a][b]
    return mat(data)

def instrument_probs(kraus: Sequence[Matrix],rho: Matrix)-> list[float]:
    return [trace(quantum_channel([k],rho)).real for k in kraus]

def projective_then_forget(rho: Matrix) -> Matrix:
    return quantum_channel([P0,P1],rho)

def random_z_then_forget(rho: Matrix)->Matrix:
    return quantum_channel([scale(1/math.sqrt(2),I),scale(1/math.sqrt(2),Z)],rho)

def sample_probe_discrepancy() -> dict:
    identity=[I]
    phase=[rz(.7)]
    return {
      'at_z0_max_difference':maxdiff(quantum_channel(identity,ZERO),quantum_channel(phase,ZERO)),
      'at_plus_max_difference':maxdiff(quantum_channel(identity,PLUS),quantum_channel(phase,PLUS)),
      'full_choi_max_difference':maxdiff(choi(identity),choi(phase)),
    }

def split_context() -> dict:
    whole=ry(.8);half=ry(.4)
    assert maxdiff(choi([whole]),choi([mul(half,half)]))<1e-12
    # If the experimental protocol permits an intermediate Z operation, one
    # may distinguish the two slot structures. No claim about fundamental ticks.
    split_with_Z=mul(mul(half,Z),half)
    no_intervention=mul(half,half)
    return {
      'coarse_channel_choi_max_difference':maxdiff(choi([whole]),choi([no_intervention])),
      'p1_without_intervention':quantum_channel([no_intervention],ZERO)[1][1].real,
      'p1_with_intermediate_Z':quantum_channel([split_with_Z],ZERO)[1][1].real,
      'intervention_channel_max_difference':maxdiff(choi([no_intervention]),choi([split_with_Z]))
    }

def kraus_relabeling() -> dict:
    p=.2
    a=scale(math.sqrt(1-p),I)
    b=scale(math.sqrt(p),Z)
    mixed=[a,b]
    rotated=[scale(1/math.sqrt(2),add(a,b)),scale(1/math.sqrt(2),add(a,scale(-1,b)))]
    return {
       'coarse_choi_max_difference':maxdiff(choi(mixed),choi(rotated)),
       'original_record_probs_on_zero':instrument_probs(mixed,ZERO),
       'rotated_record_probs_on_zero':instrument_probs(rotated,ZERO),
       'coarse_channel_same':maxdiff(choi(mixed),choi(rotated))<1e-12,
       'recorded_instruments_different':abs(instrument_probs(mixed,ZERO)[0]-instrument_probs(rotated,ZERO)[0])>.05
    }

def run_checks()->dict:
    split=split_context()
    kraus=kraus_relabeling()
    probe=sample_probe_discrepancy()
    assert split['coarse_channel_choi_max_difference'] < 1e-12
    assert split['p1_with_intermediate_Z']<1e-12
    assert split['p1_without_intervention']>.1
    assert kraus['coarse_channel_same'] and kraus['recorded_instruments_different']
    assert math.isclose(kraus['original_record_probs_on_zero'][0],.8,abs_tol=1e-12)
    assert math.isclose(kraus['rotated_record_probs_on_zero'][0],.9,abs_tol=1e-12)
    assert probe['at_z0_max_difference']<1e-12 and probe['at_plus_max_difference']>.1
    assert maxdiff(choi([I]),choi([scale(cmath.exp(1j*.9),I)]))<1e-12
    assert maxdiff(choi([I]),choi([mul(I,mul(I,I))]))<1e-12
    assert maxdiff(choi([P0,P1]),choi([scale(1/math.sqrt(2),I),scale(1/math.sqrt(2),Z)]))<1e-12
    assert maxdiff(projective_then_forget(PLUS),random_z_then_forget(PLUS))<1e-12
    return {
      'status':'PASS: standard channel/instrument identities and operational counterexamples; NOT fundamental physical events derived',
      'R7_equivalence':'Two candidate processes are equivalent only relative to all allowed inputs, interventions, outcomes, and environment records',
      'unchanged_coarse_result_can_hide_distinct_intermediate_histories':split,
      'same_average_channel_different_recorded_instruments':kraus,
      'one_probe_insufficient_to_establish_equivalence':probe,
      'global_phase_channel_invariant':True,
      'identity_splitting_does_not_define_ticks':True,
      'projective_dephasing_equals_random_z_without_record':True,
      'unresolved':[ 'Allowed operational contexts must be specified, not determined by Gamma_x',
       'A completely positive channel is an imported quantum-information primitive',
       'Equality of endpoint channels does not imply equality of histories or ontological microevents',
       'Different Kraus decompositions of one channel can correspond to distinguishable instrument outcomes when an actual measurement apparatus records them',
       'Instrument semantics cannot be read off from Kraus labels alone',
       'Non-unique event granularity prevents using operation counts as universal clock',
       'No quantum-to-GR bridge, physical time, c, hbar, microscopic clock frequency, or unique Omega measure derived']
    }

if __name__=='__main__':
    print(json.dumps(run_checks(),ensure_ascii=False,indent=2))
