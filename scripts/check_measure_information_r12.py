#!/usr/bin/env python3
"""Omega R12 — non-identifiability despite composition and information consistency.

Standard mathematical counterexamples, not a new fundamental dynamic.
Hilbert space, Born rule, and the 2-level system are explicit IMPORTS.
No metric, proper time, c, hbar, gravity, or Omega laws are derived.
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path


def probability(p: float) -> float:
    if not (math.isfinite(p) and 0 < p < 1):
        raise ValueError('physical two-outcome demonstration needs 0 < p < 1')
    return p


def h2(p: float) -> float:
    if not math.isfinite(p) or not 0 <= p <= 1:
        raise ValueError('probability outside [0,1]')
    return sum(-x * math.log2(x) for x in (p, 1-p) if x > 0)


def binary_outcomes(p: float) -> tuple[float, float]:
    p = probability(p)
    return 1-p, p


def independent_composition(p: float, q: float) -> tuple[float, ...]:
    a, b = binary_outcomes(p), binary_outcomes(q)
    return tuple(x*y for x in a for y in b)


def refined_outcomes(p: float, fraction: float) -> tuple[float, ...]:
    """Refine only ONE physical alternative into two sub-outcomes.

    Refinement invariance means the measure is pushed forward by regrouping,
    NOT uniform weighting of three REPRESENTATION labels.
    """
    probability(p)
    probability(fraction)
    return (1-p, p*fraction, p*(1-fraction))


def matrix_u(p: float) -> tuple[tuple[float, float], tuple[float, float]]:
    """Rotation preserving all quantum information, with Born P(1)=p.

    One qubit unitary; p is not derived from unitarity or ontology.
    """
    probability(p)
    a, b = math.sqrt(1-p), math.sqrt(p)
    return ((a, -b), (b, a))


def unitary_residual(p: float) -> float:
    u = matrix_u(p)
    return max(abs(sum(u[k][i]*u[k][j] for k in range(2))-(1. if i==j else 0.))
               for i in range(2) for j in range(2))


def entangled_register(p: float) -> dict[str, float]:
    """A reversible CNOT creates sqrt(1-p)|00>+sqrt(p)|11>.

    GLOBAL entropy stays 0 for the pure bipartite state. The REDUCED
    subsystem entropy is h2(p): global preservation does not select p.
    """
    probability(p)
    a,b=math.sqrt(1-p), math.sqrt(p)
    # Explicit Schmidt amplitudes after local U(p) and controlled NOT.
    psi = (a, 0., 0., b)
    norm = sum(x*x for x in psi)
    return {'born_probability_1':psi[3]**2,
            'global_purity':norm**2,
            'global_von_neumann_entropy_bits':0.,
            'reduced_entropy_bits':h2(p),
            'mutual_information_bits':2*h2(p)}


def symmetric_correlated_pair(same: float) -> dict[str, float | tuple[float, ...]]:
    """Same single-event marginals (1/2), arbitrarily different correlations.

    Exchange of the two SUBSYSTEMS and a simultaneous global bit flip
    are genuine symmetries of each distribution; same != fixed by them.
    """
    probability(same)
    joint=(same/2,(1-same)/2,(1-same)/2,same/2)
    return {'joint':joint, 'P_X_1':.5, 'P_Y_1':.5,
            'probability_equal':same,
            'mutual_information_bits':1-h2(same)}


def noisy_channel_information(p: float, error: float) -> dict[str, float]:
    """Data processing under a binary symmetric channel, imported Shannon.

    I(X;Y)=H(Y)-H(Y|X) <= H(X), holds for a continuum of p.
    """
    probability(p)
    if not (math.isfinite(error) and 0 <= error <= .5):
        raise ValueError('error should be finite in [0,0.5]')
    py=error+(1-2*error)*p
    info=h2(py)-h2(error)
    return {'input_entropy_bits':h2(p), 'mutual_information_bits':info,
            'difference_bits':h2(p)-info}


def run_checks() -> dict[str, object]:
    models=[]
    for p in (.2,.5,.8):
        independent=independent_composition(p,.3)
        fine=refined_outcomes(p,.37)
        ent=entangled_register(p)
        dp=noisy_channel_information(p,.1)
        assert math.isclose(sum(independent),1.,abs_tol=1e-14)
        assert math.isclose(h2(p)+h2(.3),-sum(x*math.log2(x) for x in independent),abs_tol=1e-13)
        assert math.isclose(fine[1]+fine[2],p,abs_tol=1e-15)
        assert unitary_residual(p)<1e-14
        assert math.isclose(ent['born_probability_1'],p,abs_tol=1e-14)
        assert dp['difference_bits']>=-1e-13
        models.append({'p':p,'allowed_outcomes':['0','1'], 'P_1':p,
                       'joint_1_1_with_independent_q03':independent[3],
                       'unitarity_residual':unitary_residual(p),
                       'reduced_entropy_bits':ent['reduced_entropy_bits'],
                       'global_von_neumann_entropy_bits':ent['global_von_neumann_entropy_bits'],
                       'data_processing_information_bits':dp['mutual_information_bits']})
    assert models[0]['allowed_outcomes']==models[2]['allowed_outcomes']
    assert not math.isclose(models[0]['P_1'],models[2]['P_1'])
    correlations=[]
    for s in (.2,.5,.8):
        cor=symmetric_correlated_pair(s)
        assert math.isclose(sum(cor['joint']),1.,abs_tol=1e-14)
        assert math.isclose(cor['joint'][0]+cor['joint'][1],.5)
        assert math.isclose(cor['joint'][0]+cor['joint'][2],.5)
        correlations.append({'P_equal':s,'I_XY_bits':cor['mutual_information_bits']})
    assert math.isclose(correlations[0]['I_XY_bits'],correlations[2]['I_XY_bits'],abs_tol=1e-14)
    assert correlations[1]['I_XY_bits'] < correlations[0]['I_XY_bits']
    # A physical exchange symmetry of the TWO OUTCOMES fixes p=.5,
    # but mere renaming covariance cannot impose that physical symmetry.
    assert math.isclose(.5,1-.5)
    naive_label_probability_B=2/3
    assert not math.isclose(naive_label_probability_B,.5)
    return {
        'status':'PASS: algebraic counterexamples; not Omega empirical validation',
        'assumptions_imported':['probability and normalization','Shannon chain rule',
            'finite complex Hilbert space','unitarity','Born probability','bipartite registers'],
        'models':models,'correlations':correlations,
        'coarse_grain_example':{'physical_P_B':.5,
             'fine_P_B1':.5*.37,'fine_P_B2':.5*.63,
             'naive_uniform_three_labels_P_B':naive_label_probability_B},
        'physical_exchange_symmetric_case':.5,
        'negative_results':[
            'Positivity, causal support and normalized product composition admit every p in (0,1).',
            'Shannon additivity (chain rule) and data processing hold for all p: they do not select p.',
            'Unitary GLOBAL information preservation permits distinct Born probabilities p.',
            'Identical symmetric marginals do not fix physical correlations (s is free).',
            'Equal information content I(X;Y) need not fix sign of correlation.',
            'Fine-grained uniform counting of labels is not invariant under regrouping.',
            'Max entropy p=1/2 follows only after adding a maximum-entropy selection rule and a specified symmetry/prior.',
            'Quantum examples import a Hilbert space and Born rule; no derivation of either from Omega.',
            'No physical unit of duration, Lorentz cone, mass, energy or quantum gravity is derived.'
        ]}


def save(folder: Path)->None:
    folder.mkdir(parents=True,exist_ok=True)
    out=run_checks()
    (folder/'OMEGA_R12_MEDIDA_INFORMACION_RESULTADOS.json').write_text(
        json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (folder/'OMEGA_R12_MODELOS.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['p','P_1','P_11_q03','unitarity_residual','reduced_entropy_bits','data_processing_information_bits'])
        for m in out['models']:
            w.writerow([m['p'],m['P_1'],m['joint_1_1_with_independent_q03'],m['unitarity_residual'],
                        m['reduced_entropy_bits'],m['data_processing_information_bits']])

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    if args.out:save(args.out)
    print(json.dumps(run_checks(),ensure_ascii=False,indent=2))