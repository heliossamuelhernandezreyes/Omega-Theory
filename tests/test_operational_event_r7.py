"""Regressions for R7 using standard quantum-channel identities; not evidence for Omega."""
import cmath
import importlib.util
import math
from pathlib import Path
import sys

source = Path(__file__).resolve().parents[1] / 'scripts' / 'check_operational_event_r7.py'
spec = importlib.util.spec_from_file_location('omega_r7', source)
M = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = M
spec.loader.exec_module(M)


def test_one_rotation_equals_two_in_coarse_channel():
    assert M.split_context()['coarse_channel_choi_max_difference'] < 1e-12


def test_intermediate_control_makes_split_history_distinguishable():
    case = M.split_context()
    assert math.isclose(case['p1_without_intervention'], math.sin(.4)**2, abs_tol=1e-12)
    assert case['p1_with_intermediate_Z'] < 1e-12


def test_noncommuting_operations_need_causal_order():
    a = M.ry(.4)
    b = M.rz(.7)
    assert M.maxdiff(M.choi([M.mul(a,b)]),M.choi([M.mul(b,a)])) > .1


def test_global_phase_does_not_make_a_new_channel():
    assert M.maxdiff(M.choi([M.I]),M.choi([M.scale(cmath.exp(.7j),M.I)])) < 1e-12


def test_identity_subdivisions_cannot_count_true_events():
    assert M.maxdiff(M.choi([M.I]),M.choi([M.mul(M.I,M.mul(M.I,M.I))])) < 1e-12


def test_kraus_unitary_remixing_preserves_coarse_choi():
    c = M.kraus_relabeling()
    assert c['coarse_channel_same']
    assert c['coarse_choi_max_difference'] < 1e-12


def test_instrument_outcomes_preserve_operational_difference():
    c = M.kraus_relabeling()
    assert math.isclose(c['original_record_probs_on_zero'][0],.8,abs_tol=1e-12)
    assert math.isclose(c['rotated_record_probs_on_zero'][0],.9,abs_tol=1e-12)
    assert c['recorded_instruments_different']


def test_same_dephasing_different_recorded_protocols():
    a=[M.P0,M.P1]
    b=[M.scale(1/math.sqrt(2),M.I),M.scale(1/math.sqrt(2),M.Z)]
    assert M.maxdiff(M.choi(a),M.choi(b)) < 1e-12
    assert math.isclose(M.instrument_probs(a,M.ZERO)[0],1.,abs_tol=1e-12)
    assert math.isclose(M.instrument_probs(b,M.ZERO)[0],.5,abs_tol=1e-12)


def test_single_input_not_process_tomography():
    r=M.sample_probe_discrepancy()
    assert r['at_z0_max_difference'] == 0.
    assert r['at_plus_max_difference'] > .3
    assert r['full_choi_max_difference'] > .6


def test_fully_equivalent_choi_on_entire_operator_basis():
    whole = M.ry(.8)
    split = M.mul(M.ry(.4),M.ry(.4))
    for i in range(2):
        for j in range(2):
            op = M.mat([[int(a==i and b==j) for b in range(2)] for a in range(2)])
            assert M.maxdiff(M.quantum_channel([whole],op),
                             M.quantum_channel([split],op))<1e-12


def test_bad_inputs_rejected():
    calls=(lambda:M.ry(float('nan')),
           lambda:M.outer_state(2,0),
           lambda:M.mat([[1],[1,2]]),
           lambda:M.quantum_channel([],M.ZERO),
           lambda:M.maxdiff(M.I,M.mat([[1]])))
    for fn in calls:
        try:
            fn()
        except ValueError:
            continue
        raise AssertionError('Invalid operation not rejected')


def test_run_checks_records_no_go():
    report=M.run_checks()
    assert report['status'].startswith('PASS')
    assert report['identity_splitting_does_not_define_ticks']
    assert any('Non-unique event granularity' in x for x in report['unresolved'])
