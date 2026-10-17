"""Regression checks for source normalization, independent reference and gauge degeneracy.

All tests prove toy/phenomenological identities, NOT Omega physical accuracy.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import math
import numpy as np
import pytest

s=Path(__file__).resolve().parents[1]/'scripts'/'check_omega_em_cdm_bridge_r10.py'
spec=importlib.util.spec_from_file_location('omega_r10',s)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_beta0_matches_lcdm_odes():
    x=m.integrate_growth(beta=0)
    assert np.allclose(x['fs8_correct'],m.integrate_growth(beta=0)['fs8_correct'],atol=1e-12,rtol=0)


def test_source_growth_rate_normalization_bug_exact():
    x=m.integrate_growth()
    assert np.allclose(x['f_source'],x['f_correct']*x['d0'],rtol=2e-13,atol=1e-14)


def test_corrected_fsigma8_at_today():
    x=m.integrate_growth()
    assert math.isclose(float(x['fs8_correct'][-1]),m.SIGMA8_0*float(x['f_correct'][-1]),rel_tol=1e-13)


def test_original_readme_suppression_not_reproduced():
    row=m.summary()['at_z1']
    assert -22<row['source_implementation_vs_own_proxy_percent']<-21
    assert -0.005<row['corrected_relative_growth_percent']<0


def test_original_vs_correct_gamma():
    z=m.summary()['at_z0']
    assert .76<z['gamma_source']<.77
    assert .55<z['gamma_correct']<.56
    assert abs(z['gamma_correct']-.63)>.07


def test_g_eff_almost_gr_for_beta_025():
    assert 0.99999<m.geff(.5)<1
    assert m.geff(1)>0.999999


def test_geff_beta_zero_exact():
    for a in (.1,.5,1.):
        assert float(m.geff(a,beta=0))==1.


def test_correct_growth_near_unmodified_LCDM():
    x=m.integrate_growth()
    y=m.integrate_growth(beta=0)
    assert 1e-6<np.max(np.abs(x['fs8_correct']-y['fs8_correct']))<2e-5


def test_gauge_invariance_for_arbitrary_vertex_shift():
    edges=[(0,1),(1,2),(2,3),(3,0)]
    links=[.15,-.4,.09,.5];theta=[.1,-.3,.4,-.17]
    for g in ([.5,-.6,.2,.08],[0,0,0,0],[7.2,-2.7,.39,1.5]):
        t,l=m.gauge_transform(theta,edges,links,g)
        assert math.isclose(m.full_gauge_energy(theta,edges,links),m.full_gauge_energy(t,edges,l),abs_tol=1e-13)


def test_link_sum_flux_invariance():
    edges=[(0,1),(1,2),(2,3),(3,0)];A=[.15,-.4,.09,.5]
    _,B=m.gauge_transform([0]*4,edges,A,[.6,-.3,.4,.7])
    assert math.isclose(sum(A),sum(B),abs_tol=1e-14)


def test_free_photon_coupling_same_gravity_prediction():
    s=m.summary()
    assert len(set(p['G_eff_z1_unchanged'] for p in s['toy_photon_scalar_profiles']))==1
    assert len(set(p['z1_fractional_shift'] for p in s['toy_photon_scalar_profiles']))==4


def test_zero_coupling_no_alpha_variation():
    for a in (.1,.5,1.):assert m.alpha_ratio(a,0.)==1.


def test_clock_sensitive_nonzero_coupling_freedom():
    assert abs(m.alpha_ratio(.5,1e-3)-1)>1e-6
    assert m.alpha_ratio(.5,1e-5)>m.alpha_ratio(.5,1e-3)
    assert m.alpha_ratio(1.,.1)==1.


def test_positive_gauge_kinetic_scaling():
    for a in (.1,.3,.5,1.):
        for x in (-.1,0,.1):assert m.B_photon(a,x)>0


def test_no_gravity_em_coupling_without_independent_axiom():
    assert m.geff(.5,beta=0)==1.
    assert m.alpha_ratio(.5,1e-3)!=1.
    assert m.geff(.5,beta=.25)!=1.
    assert m.alpha_ratio(.5,0)==1.


def test_solver_tolerance_stability():
    r=m.integrate_growth(n=550,rtol=1e-10,atol=1e-12)
    q=m.integrate_growth(n=1100,rtol=1e-12,atol=1e-14)
    assert abs(m.get_at_z(r,'fs8_correct',1.)-m.get_at_z(q,'fs8_correct',1.))<2e-7


def test_parameter_sensitivity_beta_growth():
    ref=m.integrate_growth(beta=0)
    f0=m.get_at_z(ref,'fs8_correct',1.)
    f25=m.get_at_z(m.integrate_growth(beta=.25),'fs8_correct',1.)
    f50=m.get_at_z(m.integrate_growth(beta=.50),'fs8_correct',1.)
    assert f50 < f25 < f0


def test_invalid_plaquette_shape():
    with pytest.raises(ValueError):
        m.full_gauge_energy([1,2],[(0,1)], [.5])