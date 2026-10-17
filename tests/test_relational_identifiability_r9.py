"""R9 assertions; all results conditional, synthetic, not evidence for Omega."""
import importlib.util
import math
from pathlib import Path
import sys

PATH=Path(__file__).resolve().parents[1]/'scripts'/'check_relational_identifiability_r9.py'
spec=importlib.util.spec_from_file_location('omega_r9',PATH)
M=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=M
spec.loader.exec_module(M)


def test_unitarity_of_each_rotation():
    for theta in (.0,.2,.46,1.2):
        a=M.rotation_y(theta)
        assert math.isclose(a[0][0]**2+a[1][0]**2,1)
        assert math.isclose(a[0][1]**2+a[1][1]**2,1)
        assert math.isclose(a[0][0]*a[0][1]+a[1][0]*a[1][1],0,abs_tol=1e-14)

def test_composition_identity():
    for t in (.22,.37,.46):
        assert M.max_matrix_difference(M.matmul(M.rotation_y(t/2),M.rotation_y(t/2)),M.rotation_y(t))<1e-15

def test_same_causal_graph_different_ratios():
    x=M.run_checks()['nonidentifiability_witnesses']
    assert x[0]['graph']==x[1]['graph']
    assert abs(x[0]['theoretical_ratio']-x[1]['theoretical_ratio'])>.4

def test_recover_phase_held_out_from_XZ():
    assert math.isclose(M.recover_phase_from_two_quadratures(M.trajectory(.318)),.318,abs_tol=1e-12)

def test_recover_ratio_from_observations_not_input():
    a,b=M.trajectory(.22),M.trajectory(.37)
    assert math.isclose(M.relative_ratio_from_data(a,b),.22/.37)

def test_identical_clocks_exchange_symmetric_ratio_one():
    assert M.identical_local_structure(.37,.37)['exchange_symmetric_when_equal']
    assert M.relative_ratio_from_data(M.trajectory(.37),M.trajectory(.37))==1

def test_unequal_clocks_not_exchange_symmetric():
    assert not M.identical_local_structure(.22,.37)['exchange_symmetric_when_equal']

def test_irregular_refinement_preserves_coarse_measurements():
    all_,coarse=M.refine_trajectory(.22,(.1,.2,.7))
    original=M.trajectory(.22)
    assert len(all_)==25 and len(coarse)==len(original)
    assert max(abs(x['X']-y['X']) for x,y in zip(coarse,original))<1e-14

def test_different_refinements_preserve_ratio():
    _,a=M.refine_trajectory(.22,(.1,.2,.7))
    _,b=M.refine_trajectory(.37,(.2,.25,.55))
    assert math.isclose(M.relative_ratio_from_data(a,b),.22/.37)

def test_no_alias_free_absolute_frequency():
    assert M.precision_alias(.22)<7e-15

def test_single_quadrature_loses_sign():
    assert M.single_quadrature_alias(.22)==0

def test_sampling_beyond_principal_branch_returns_alias():
    assert math.isclose(M.recover_phase_from_two_quadratures(M.trajectory(.22+2*math.pi)),.22,abs_tol=1e-12)

def test_reparameterization_invariance_is_not_new_dynamics():
    assert M.dimensionless_reparameterization(.22,.37,7)<1e-14

def test_invalid_or_nonstationary_observations():
    for work in (lambda:M.trajectory(float('nan')),lambda:M.trajectory(.1,n=1),
                 lambda:M.refine_trajectory(.2,(.2,.2)),
                 lambda:M.recover_phase_from_two_quadratures(M.trajectory(.22)[:1]),
                 lambda:M.recover_phase_from_two_quadratures([{'X':0,'Z':1},{'X':0.5,'Z':1}])):
        try:work()
        except ValueError:pass
        else:raise AssertionError('expected ValueError')

def test_no_Omega_prediction_claimed():
    r=M.run_checks()
    assert 'NO derivation' in r['status']
    assert len(r['remaining_undetermined'])>=6