#!/usr/bin/env python3
"""Omega R8: no-go theorem & conditional correlations between quantum clocks.

All matrix physics is conventional finite-dimensional QM. No fundamental time,
clock pace, GR metric, Born measure, hbar, or actual Omega law is derived.
The clock-register labels and rotation angles are explicit assumptions.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np


ZERO = np.array([1., 0.], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
X = np.array([[0., 1.], [1., 0.]], dtype=complex)


def ry(phi: float) -> np.ndarray:
    if not math.isfinite(phi):
        raise ValueError('angle must be finite')
    c, s = math.cos(phi/2), math.sin(phi/2)
    return np.array([[c, -s], [s, c]], dtype=complex)


def pure_bures_angle(a: np.ndarray, b: np.ndarray) -> float:
    """Fubini-Study angle arccos |<a|b>|; endpoint, not duration."""
    overlap = abs(np.vdot(a, b))
    return math.acos(min(1., max(0., float(overlap))))


def qubit_observables(state: np.ndarray) -> dict:
    return {'p_one': float(abs(state[1])**2),
            'x': float(np.real(np.vdot(state, X@state))),
            'z': float(np.real(np.vdot(state, Z@state)))}


def history_amplitudes(num_readings: int, angle_A: float, angle_B: float,
                       refinement: int = 1) -> np.ndarray:
    """Array of normalized conditional states indexed by an explicit clock label.

    For refinement r>1 the clock contains intermediate labels 0..(N-1)*r.
    Each local half-action is split uniformly. The coarse labels j*r have
    exactly the same conditional quantum states as the unrefined history.
    """
    if num_readings < 2 or refinement < 1:
        raise ValueError('need >=2 readings and refinement >=1')
    if not (math.isfinite(angle_A) and math.isfinite(angle_B)):
        raise ValueError('finite angles only')
    uA = ry(angle_A/refinement)
    uB = ry(angle_B/refinement)
    u = np.kron(uA, uB)
    total_steps=(num_readings-1)*refinement
    out=np.empty((total_steps+1, 4), dtype=complex)
    state=np.kron(ZERO, ZERO)
    for j in range(total_steps+1):
        out[j]=state
        state=u@state
    return out


def relational_observables(conditional: np.ndarray) -> list[dict]:
    rows=[]
    for j,psi in enumerate(conditional):
        tensor=psi.reshape((2,2))
        rho_A=tensor@tensor.conj().T
        rho_B=tensor.conj().T@tensor
        pA=float(np.real(rho_A[1,1]));pB=float(np.real(rho_B[1,1]))
        xA=float(np.real(np.trace(rho_A@X)));zA=float(np.real(np.trace(rho_A@Z)))
        xB=float(np.real(np.trace(rho_B@X)));zB=float(np.real(np.trace(rho_B@Z)))
        phiA=math.atan2(xA,zA);phiB=math.atan2(xB,zB)
        rows.append({'reference_clock_label':j,
                     'P_A_one_given_reference':pA,
                     'P_B_one_given_reference':pB,
                     'phase_A_from_XZ':phiA,'phase_B_from_XZ':phiB,
                     'relative_phase_A_over_B':phiA/phiB if abs(phiB)>1e-12 else None})
    return rows


def stationary_history_constraint_norm(conditional: np.ndarray, angle_A: float,
                                        angle_B: float, refinement: int = 1) -> float:
    """Propagation constraint (Feynman history-state analogue).

    |Psi>=sum_j |j>|psi_j>/sqrt(N). H_prop=sum_j L_j^dag L_j,
    where L_j|Psi>=(|psi_(j+1)>-U|psi_j>)/sqrt(N). Thus H_prop>=0
    and H_prop|Psi>=0 when all residuals vanish. Clock labels are ASSUMED.
    """
    u=np.kron(ry(angle_A/refinement), ry(angle_B/refinement))
    residuals=conditional[1:]-conditional[:-1]@u.T
    return float(np.linalg.norm(residuals))


def probe_insertion_distinction(phi: float = .8) -> dict:
    """U(phi) vs U(phi/2) Z U(phi/2). Intermediate intervention matters."""
    without=ry(phi)@ZERO
    with_probe=ry(phi/2)@Z@ry(phi/2)@ZERO
    return {'uninterrupted_P_one':float(abs(without[1])**2),
            'Z_intervention_P_one':float(abs(with_probe[1])**2),
            'same_experiment':False}


def endpoint_loop_ambiguity(phi: float = .8) -> dict:
    """Identity and U^{-1}U same channel; nontrivial sampled path."""
    initial=ZERO
    middle=ry(phi)@initial
    end=ry(-phi)@middle
    direct_angle=pure_bures_angle(initial,end)
    # two successive legs give a nonzero geometrical path length
    leg_a=pure_bures_angle(initial,middle)
    leg_b=pure_bures_angle(middle,end)
    return {'endpoint_angle':direct_angle,
            'measured_two_leg_path_angle':leg_a+leg_b,
            'middle_P_one':float(abs(middle[1])**2),
            'end_P_one':float(abs(end[1])**2)}


def check_no_go(reversible_angles=(.2,.8,1.4)) -> dict:
    """Algebraic no-go independent of sampled values.

    D: unitary channels -> nonnegative reals; D(I)=0;
    D(VU)=D(V)+D(U); invariance under changing the representation.
    0=D(U^-1 U)=D(U^-1)+D(U) => D(U)=0.
    The following numerical values merely illustrate this proof.
    """
    vals=[]
    for phi in reversible_angles:
        identity=ry(-phi)@ry(phi)
        vals.append({'phi':phi,'max_identity_matrix_error':float(np.max(np.abs(identity-np.eye(2))))})
    return {'proof':'Nonnegative additive endpoint-only duration must vanish on all reversible channels.',
            'examples':vals}


def run_checks() -> dict:
    n=7; a=.20;b=.35; ref=4
    coarse=history_amplitudes(n,a,b)
    fine=history_amplitudes(n,a,b,ref)
    picked=fine[::ref]
    difference=float(np.max(np.abs(coarse-picked)))
    assert difference<1e-13
    assert np.allclose(np.linalg.norm(coarse,axis=1),1,atol=1e-13)
    assert np.allclose(np.linalg.norm(fine,axis=1),1,atol=1e-13)
    # A globally stationary pure history state exists by construction.
    global_normalized=coarse.reshape(-1)/math.sqrt(n)
    assert math.isclose(float(np.vdot(global_normalized,global_normalized).real),1,abs_tol=1e-13)
    constraint=stationary_history_constraint_norm(coarse,a,b)
    assert constraint<1e-13
    obs=relational_observables(coarse)
    for j,row in enumerate(obs):
        assert math.isclose(row['P_A_one_given_reference'],math.sin(j*a/2)**2,abs_tol=1e-13)
        assert math.isclose(row['P_B_one_given_reference'],math.sin(j*b/2)**2,abs_tol=1e-13)
        if j:
            assert math.isclose(row['relative_phase_A_over_B'],a/b,abs_tol=2e-13)
    p=probe_insertion_distinction()
    assert math.isclose(p['uninterrupted_P_one'],math.sin(.4)**2,abs_tol=1e-14)
    assert abs(p['Z_intervention_P_one'])<1e-14
    loop=endpoint_loop_ambiguity()
    assert loop['endpoint_angle']<1e-7
    assert math.isclose(loop['measured_two_leg_path_angle'],.8,abs_tol=1e-7)
    assert loop['middle_P_one']>.15 and loop['end_P_one']<1e-14
    # An endpoint-only fidelity is not additive on an inverse loop.
    # Splitting within the same physical slots is equivalent; granting
    # access to intermediate labels makes it a DIFFERENT intervention context.
    return {'status':'PASS: finite-dimensional quantum toy identities, NOT physical Omega derivation',
            'theorem':check_no_go(),
            'setup':{'clock_register_readings_assumed':n,
                     'refinement_factor':ref,
                     'coarse_clock_register_dimension':n,
                     'fine_clock_register_dimension':len(fine),
                     'rotations_per_coarse_step':{'A_radians':a,'B_radians':b},
                     'initial_A_and_B':'|0> ⊗ |0>'},
            'refinement_max_coarse_state_difference':difference,
            'history_constraint_residual_norm':constraint,
            'relative_phase_frequency_ratio_derived_from_assumed_angles':a/b,
            'conditional_clock_observables':obs,
            'probe_insertion':p,
            'inverse_loop':loop,
            'limitations':[
             'The label j is a user-chosen quantum clock register, not derived time.',
             'Rotation angles and Born probabilities are imported from standard quantum mechanics.',
             'Equality on selected coarse clock readings does not imply the entire fine history is operationally equivalent.',
             'An unobserved inverse loop can have zero endpoint distance but nonzero probed history.',
             'The nonnegative additive endpoint-only duration no-go covers reversible unitary dynamics, not relational durations depending on clock/environment.',
             'Phase ratios are conditional on the input angles and phase reference; angles can wrap, clocks need calibration.',
             'No Lorentz invariance, gravitation, metric time, omega fundamental law, mass, speed c or Planck scale derived.'
            ]}


def save(path: Path) -> dict:
    result=run_checks()
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    return result

if __name__=='__main__':
    arg=argparse.ArgumentParser()
    arg.add_argument('--out',type=Path)
    args=arg.parse_args()
    r=save(args.out) if args.out else run_checks()
    print(json.dumps(r,indent=2,ensure_ascii=False))
