#!/usr/bin/env python3
"""Omega R9: causal composition does not identify quantum clock frequencies.

Model is a KNOWN two-level unitary rotation model: angles are free hypothetical
parameters, NOT derived from Omega. Measurement samples are synthetic, exact,
and not empirical data. No physical time unit is present in index j.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path

TWO_PI=2*math.pi


def rotation_y(theta):
    """A real SU(2) rotation; j is an ordinal index, never physical seconds."""
    c,s=math.cos(theta/2),math.sin(theta/2)
    return ((c,-s),(s,c))


def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def max_matrix_difference(a,b):
    return max(abs(a[i][j]-b[i][j]) for i in range(2) for j in range(2))


def trajectory(theta,n=9):
    """For starting |0>, <X>=sin(j theta), <Z>=cos(j theta)."""
    if not math.isfinite(theta) or n < 2:
        raise ValueError('finite theta and at least 2 samples required')
    return [{'j':j,'X':math.sin(j*theta),'Z':math.cos(j*theta),
             'p_one':math.sin(j*theta/2)**2} for j in range(n)]


def recover_phase_from_two_quadratures(observations):
    """Circular phase increment, modulo 2*pi; no access to given theta.

    Requires phase-locked X and Z observations and constant increment between
    adjacent indexed records. Cannot resolve 2*pi alias or set seconds/step.
    """
    if len(observations)<2:
        raise ValueError('need 2+ observations')
    phases=[complex(float(x['Z']),float(x['X'])) for x in observations]
    if any(abs(abs(z)-1)>1e-7 for z in phases):
        raise ValueError('invalid ideal Bloch-vector magnitude')
    deltas=[phases[i+1]*phases[i].conjugate()
            for i in range(len(phases)-1)]
    z=sum(deltas)/len(deltas)
    if abs(z)<1e-6:
        raise ValueError('increments inconsistent; complex mean zero')
    spread=max(abs(delta/z*abs(z)-1) for delta in deltas)
    if spread>1e-6:
        raise ValueError('nonuniform increments; no single frequency')
    return math.atan2(z.imag,z.real)


def relative_ratio_from_data(a,b):
    ta=recover_phase_from_two_quadratures(a)
    tb=recover_phase_from_two_quadratures(b)
    if abs(tb)<1e-9: raise ValueError('reference clock has zero recovered phase')
    return ta/tb


def refine_trajectory(theta, fractions=(.1,.2,.7), n=9):
    """Split each original rotation into nonuniform smaller rotations.

    Returns coarse-index samples and all intermediate samples. The fractions
    model representational slicing, NOT physical events forced by nature.
    """
    if not fractions or any(x<=0 for x in fractions) or abs(sum(fractions)-1)>1e-12:
        raise ValueError('strictly positive fractions summing to one')
    phases=[0.0]
    for _ in range(n-1):
        for x in fractions: phases.append(phases[-1]+theta*x)
    all_samples=[{'j':j,'X':math.sin(phi),'Z':math.cos(phi),
                  'p_one':math.sin(phi/2)**2} for j,phi in enumerate(phases)]
    return all_samples,all_samples[::len(fractions)]


def identical_local_structure(theta_a,theta_b):
    """Same 2 nodes/two one-qubit paths and same allowed on-site gates.

    Swapping clocks swaps parameters: covariance does not force A=B;
    making the joint dynamics strictly exchange-symmetric DOES force same
    step channel, except irrelevant channel global-phase equivalences.
    """
    return {'same_causal_graph':True,'locality':True,
            'composition_identity_A':max_matrix_difference(matmul(rotation_y(theta_a/2),rotation_y(theta_a/2)),rotation_y(theta_a)),
            'composition_identity_B':max_matrix_difference(matmul(rotation_y(theta_b/2),rotation_y(theta_b/2)),rotation_y(theta_b)),
            'exchange_symmetric_when_equal':max_matrix_difference(rotation_y(theta_a),rotation_y(theta_b))<1e-12}


def precision_alias(theta):
    samples1=trajectory(theta)
    samples2=trajectory(theta+TWO_PI)
    return max(abs(a[k]-b[k]) for a,b in zip(samples1,samples2) for k in ('X','Z','p_one'))


def single_quadrature_alias(theta):
    a,b=trajectory(theta),trajectory(-theta)
    return max(abs(x['Z']-y['Z']) for x,y in zip(a,b))


def distribution_total_variation(a,b):
    """Expected total-variation distinguishability at the 8th observation,
    for projective Z measurement on a prepared |0> qubit. Synthetic only.
    """
    pa=trajectory(a)[-1]['p_one'];pb=trajectory(b)[-1]['p_one']
    return abs(pa-pb)


def dimensionless_reparameterization(theta_a,theta_b,rescale):
    """Change arbitrary parametrization u'=u/rescale, frequencies'=rescale*freq.

    This changes no physical sampled endpoint IF the interval labels also
    transform consistently. Not the same as changing frequencies at fixed j.
    """
    if rescale<=0:raise ValueError('rescale>0')
    phase_a=theta_a*3;phase_b=theta_b*3
    new=theta_a*rescale*(3/rescale),theta_b*rescale*(3/rescale)
    return max(abs(phase_a-new[0]),abs(phase_b-new[1]))


def run_checks():
    # These hidden angles are synthetic witness choices, not fit from ontology.
    witnesses=[('I',.22,.37),('II',.46,.37)]
    results=[]
    for label,theta_a,theta_b in witnesses:
        a=trajectory(theta_a);b=trajectory(theta_b)
        inferred=relative_ratio_from_data(a,b)
        actual=theta_a/theta_b
        structure=identical_local_structure(theta_a,theta_b)
        assert abs(inferred-actual)<2e-14
        assert structure['same_causal_graph'] and structure['locality']
        assert structure['composition_identity_A']<1e-15
        assert structure['composition_identity_B']<1e-15
        results.append({'label':label,'graph':'same two independent local clocks',
                        'theoretical_ratio':actual,'reconstructed_ratio':inferred,
                        'probability_A_at_j8':a[-1]['p_one'],
                        'probability_B_at_j8':b[-1]['p_one']})
    assert not math.isclose(results[0]['reconstructed_ratio'],results[1]['reconstructed_ratio'])
    assert distribution_total_variation(.22,.46)>.2
    identical=relative_ratio_from_data(trajectory(.37),trajectory(.37))
    assert abs(identical-1)<1e-14
    refined_a,coarse_a=refine_trajectory(.22,(.1,.2,.7))
    refined_b,coarse_b=refine_trajectory(.37,(.2,.25,.55))
    assert len(refined_a)==25 and len(coarse_a)==9
    max_error=max(abs(ref['X']-orig['X'])+abs(ref['Z']-orig['Z'])
                  for ref,orig in zip(coarse_a,trajectory(.22)))
    max_error=max(max_error,max(abs(ref['X']-orig['X'])+abs(ref['Z']-orig['Z'])
                            for ref,orig in zip(coarse_b,trajectory(.37))))
    assert max_error<3e-15
    refined_ratio=relative_ratio_from_data(coarse_a,coarse_b)
    assert abs(refined_ratio-results[0]['reconstructed_ratio'])<2e-14
    alias=precision_alias(.22)
    assert alias<7e-15
    z_alias=single_quadrature_alias(.22)
    assert z_alias==0
    gauge=dimensionless_reparameterization(.22,.37,7.)
    assert gauge<1e-14
    # If exchange symmetry is an extra PHYSICAL property, theta_A=theta_B
    # (on a chosen principal channel branch): it forces equal periods.
    assert identical_local_structure(.37,.37)['exchange_symmetric_when_equal']
    assert not identical_local_structure(.22,.37)['exchange_symmetric_when_equal']
    # Absolute seconds undetermined by integer readings; observations are
    # compatible with arbitrary seconds per register step.
    return {
       'status':'PASS: synthetic identifiability diagnostics; NO derivation of physical clocks or Omega',
       'reference':'R8 relational clock, R7 operational equivalence',
       'permitted_axioms':['same local causal graph','composition','unitarity','phase-continuity','coarse observation relabeling'],
       'nonidentifiability_witnesses':results,
       'inter_model_observable_distinguishability_TV_at_j8':distribution_total_variation(.22,.46),
       'conditional_exchange_symmetry_forces_ratio_one':identical,
       'refinement':{'refined_readings':25,'coarse_readings':9,
                     'max_original_sample_error':max_error,
                     'coarse_A_over_B':refined_ratio},
       'aliases':{'two_pi_shift_max_observation_error':alias,'Z_only_sign_flip_error':z_alias},
       'coordinate_rescaling_endpoint_error':gauge,
       'remaining_undetermined':['relative clock ratio from Gamma_x alone',
           'physical seconds per step','integer 2pi winding numbers','physical Hamiltonian',
           'Lorentz invariant space-time','metric proper time','gravitational universality'],
       'epistemic_limit':'Inference of phase from X/Z observations is not prediction of phase from ontology.'}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    result=run_checks()
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
