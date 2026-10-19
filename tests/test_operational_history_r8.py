"""Omega R8 rigorous test suite: toy model verification, not empirical checks."""
import importlib.util
import math
import sys
from pathlib import Path
import numpy as np
import pytest

p=Path(__file__).resolve().parents[1]/'scripts'/'check_operational_history_r8.py'
spec=importlib.util.spec_from_file_location('omega_R8',p)
M=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=M
spec.loader.exec_module(M)


def test_ry_unitarity_and_inverse():
    for x in (.2,.8,1.4):
        assert np.allclose(M.ry(-x)@M.ry(x),np.eye(2),atol=1e-14)


def test_no_go_requires_nonnegative_additive_endpoint_function():
    proof=M.check_no_go()
    assert 'vanish' in proof['proof']
    assert max(x['max_identity_matrix_error'] for x in proof['examples'])<1e-14


def test_refinement_for_observations_at_original_readings():
    original=M.history_amplitudes(7,.2,.35)
    for refinement in (1,2,3,4,8):
        refined=M.history_amplitudes(7,.2,.35,refinement)
        assert np.allclose(original,refined[::refinement],atol=1e-13)


def test_unitarity_of_entire_conditional_history():
    state=M.history_amplitudes(7,.2,.35)
    assert np.allclose(np.linalg.norm(state,axis=1),1,atol=1e-13)
    assert np.isclose(np.linalg.norm(state.reshape(-1)/math.sqrt(7)),1,atol=1e-13)


def test_stationary_history_propagation_constraints():
    for r in (1,2,4):
        history=M.history_amplitudes(7,.2,.35,r)
        assert M.stationary_history_constraint_norm(history,.2,.35,r)<1e-12


def test_born_conditional_probabilities_two_systems():
    rows=M.relational_observables(M.history_amplitudes(7,.2,.35))
    for row in rows:
        j=row['reference_clock_label']
        assert math.isclose(row['P_A_one_given_reference'],math.sin(.2*j/2)**2,abs_tol=1e-13)
        assert math.isclose(row['P_B_one_given_reference'],math.sin(.35*j/2)**2,abs_tol=1e-13)


def test_relative_phase_ratio_from_two_observables_not_one():
    rows=M.relational_observables(M.history_amplitudes(7,.2,.35))
    for row in rows[1:]:
        assert math.isclose(row['relative_phase_A_over_B'],4/7,abs_tol=1e-12)


def test_intermediate_intervention_reveals_different_protocol():
    p=M.probe_insertion_distinction()
    assert p['uninterrupted_P_one']>.15
    assert p['Z_intervention_P_one']<1e-13
    assert p['same_experiment'] is False


def test_inverse_loop_endpoint_ambiguity():
    x=M.endpoint_loop_ambiguity()
    assert x['endpoint_angle']<1e-7
    assert math.isclose(x['measured_two_leg_path_angle'],.8,abs_tol=1e-7)
    assert x['middle_P_one']>.15
    assert x['end_P_one']<1e-13


def test_phase_aliasing_long_clock():
    # U_y(2*pi) is -I (global phase on a qubit), same density as I.
    st=M.ry(2*math.pi)@M.ZERO
    assert abs(np.vdot(st,M.ZERO))>=1-1e-14
    assert M.pure_bures_angle(M.ZERO,st)<1e-7


def test_history_dimension_changes_if_extra_slots_exposed():
    coarse=M.history_amplitudes(7,.2,.35)
    fine=M.history_amplitudes(7,.2,.35,4)
    assert coarse.shape==(7,4)
    assert fine.shape==(25,4)
    assert np.allclose(coarse,fine[::4],atol=1e-13)


def test_invalid_history_arguments():
    for f in (lambda:M.history_amplitudes(1,.2,.3),
              lambda:M.history_amplitudes(7,.2,.3,0),
              lambda:M.ry(float('nan'))):
        with pytest.raises(ValueError):f()


def test_deterministic_reproduction_and_qualifications():
    x=M.run_checks();y=M.run_checks()
    assert x==y
    assert x['status'].startswith('PASS')
    assert any('NOT' in x['status'] for _ in [0])
    assert x['refinement_max_coarse_state_difference']<1e-13
    assert len(x['limitations'])>=5
