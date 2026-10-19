import math
import importlib.util
from pathlib import Path

spec=importlib.util.spec_from_file_location('omega_r5',Path(__file__).resolve().parents[1]/'scripts'/'check_single_generator_r5.py')
M=importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

def test_unitary_25_steps():
    for theta in (0,.15,.3,.6):
        for n,norm,leak,right,left in M.localized_run(theta):
            assert abs(norm-1)<2e-13
            assert leak==0
            assert right>=0 and left>=0

def test_massless_moves_at_front_and_no_spin_clock():
    tr=M.localized_run(0,25)
    assert math.isclose(tr[-1][3],1)
    assert math.isclose(M.spin_clock_probability(10,0),1)

def test_spectral_dispersion():
    for k in (.1,.5,1,math.pi/2):
        for theta in (0,.1,.3,.6):
            w=M.quasi_energy(k,theta)
            assert math.isclose(math.cos(w),math.cos(k)*math.cos(theta),abs_tol=1e-13)

def test_group_speeds_not_fundamental_clock_frequency():
    assert math.isclose(M.group_velocity(math.pi/2,.3),math.cos(.3))
    assert M.group_velocity(math.pi/2,.3)>M.group_velocity(math.pi/2,.6)
    assert math.pi/.3>math.pi/.6

def test_lattice_preferred_frame():
    assert abs(M.quasi_energy(1,.5)-math.hypot(1,.5))>.03

def test_small_wave_vector_recovers_relativistic_shape_conditionally():
    rows=M.continuum_extrapolation()
    assert abs(rows[-1]['relative_error']) < 1e-4
    assert abs(rows[-1]['relative_error']) < abs(rows[0]['relative_error'])

def test_generator_is_not_timeless():
    output=M.run_checks()
    assert 'CONDITIONAL' in output['status']
    assert any('EXTERNAL' in x for x in output['negative_results'])

def test_invalid_cases():
    for call in (lambda:M.quasi_energy(0,math.pi/2),lambda:M.coin_step([1],[0],.1),
                 lambda:M.spin_clock_probability(-1,.1)):
        try: call()
        except ValueError: pass
        else: raise AssertionError('input validation failed')
