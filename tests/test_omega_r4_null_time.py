"""Algebraic regression tests; no physical validation of Omega."""
import importlib.util,sys,math
from pathlib import Path
p=Path(__file__).resolve().parents[1] / 'scripts' / 'check_omega_r4_null_time.py'
spec=importlib.util.spec_from_file_location('omega_r4',p)
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)

def test_null_limit_is_not_photon_rest_frame():
    assert m.proper_factor(1)==0 and m.proper_factor(0)==1
    assert math.isclose(m.proper_factor(.6),.8)

def test_null_modes_same_c_different_frequency():
    assert m.continuum(1,0)==(1,1) and m.continuum(2,0)==(2,1)

def test_mass_gap_reduces_group_speed_not_fundamental_c():
    assert m.continuum(1,1)[1]<m.continuum(1,0)[1]

def test_quantum_rate_depends_on_energy_spread():
    assert math.isclose(m.quantum_bound(1)/m.quantum_bound(1000),1000)

def test_lattice_breaks_exact_lorentz_at_finite_spacing():
    assert m.lattice(1)[1]<m.lattice(.1)[1]
    assert abs(m.lattice(1)[0]**2-1)>.08

def test_shared_clock_lapse_independent_of_clock_internals():
    assert m.two_clocks(.3,1,2)['frequency_ratio']==m.two_clocks(.7,1,2)['frequency_ratio']==.5

def test_number_of_paths_not_unique_kinetic_lag():
    x=m.serial_parallel(4)
    assert x['serial_effective_rate']==.25 and x['parallel_first_event_rate']==4

def test_diamond_needs_scale_and_imported_geometry():
    d=m.diamond(5,3,100)
    assert d['expected_event_count']==800 and d['proper_time_imported']==4
    assert math.sqrt(2*d['expected_event_count']/400)==2

def test_invalid_parameters_rejected():
    for f,arg in [(m.proper_factor,1.1),(m.quantum_bound,0),(m.lattice,4)]:
        try: f(arg)
        except ValueError: pass
        else: raise AssertionError('Expected ValueError')

def test_full_reproducibility():
    assert m.run()==m.run()
