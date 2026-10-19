#!/usr/bin/env python3
"""Omega R4: compare light-cones, quantum evolution, kinetic lag and clocks.
ALL inputs imported from SR/QM or illustrative toy assumptions, not Omega derivation.
"""
import json, math
HBAR_EV_S = 6.582119569e-16

def proper_factor(beta):
    if not math.isfinite(beta) or not 0 <= beta <= 1: raise ValueError('beta')
    return math.sqrt((1-beta)*(1+beta))

def continuum(k,gap):
    if not math.isfinite(k) or not math.isfinite(gap) or k<=0 or gap<0: raise ValueError('dispersion')
    w=math.hypot(k,gap)
    return w,k/w

def lattice(k):
    if not math.isfinite(k) or not 0<k<=math.pi: raise ValueError('k')
    return 2*math.sin(k/2),math.cos(k/2)

def quantum_bound(delta_e_ev):
    if not math.isfinite(delta_e_ev) or delta_e_ev<=0: raise ValueError('delta_e_ev')
    return math.pi*HBAR_EV_S/(2*delta_e_ev)

def two_clocks(common_lapse,local_A,local_B):
    if not (0<common_lapse<=1 and local_A>0 and local_B>0): raise ValueError('clock')
    return {'remote_A':common_lapse*local_A, 'remote_B':common_lapse*local_B,
            'frequency_ratio':local_A/local_B}

def serial_parallel(n,rate=1.):
    if n<1 or rate<=0: raise ValueError('rate')
    return {'serial_effective_rate':rate/n, 'parallel_first_event_rate':n*rate}

def diamond(dt,dx,rho):
    """Minkowski metric/c=1 and event density rho are ASSUMED, not derived."""
    if not (dt>abs(dx) and rho>0): raise ValueError('timelike')
    tau=math.sqrt(dt*dt-dx*dx);N=rho*tau*tau/2
    return {'proper_time_imported':tau,'expected_event_count':N,
            'proper_time_with_density_assumed':math.sqrt(2*N/rho)}

def run():
    beta=[0.,.6,.9,.99,1.]
    factors=[{'v_over_c':x,'dtau_over_dt':proper_factor(x)} for x in beta]
    assert math.isclose(factors[1]['dtau_over_dt'],.8)
    assert factors[-1]['dtau_over_dt']==0.
    # Same c for two massless modes; unequal coordinate-frame omega.
    massless_1=continuum(1,0);massless_2=continuum(2,0)
    massive=continuum(1,1)
    assert massless_1==(1.,1.) and massless_2==(2.,1.)
    assert math.isclose(massive[1],1/math.sqrt(2))
    bounds={str(v):quantum_bound(v) for v in (1.,1e3,1e6)}
    assert math.isclose(bounds['1.0']/bounds['1000.0'],1000.)
    lattice_cases={str(k):{'vg_over_c':lattice(k)[1],
        'relative_dispersion_sq_error':lattice(k)[0]**2/k**2-1} for k in (.1,1.,2.)}
    assert lattice_cases['1.0']['relative_dispersion_sq_error'] < -.08
    assert lattice_cases['2.0']['vg_over_c'] < lattice_cases['0.1']['vg_over_c']
    clocks=two_clocks(.4,1.,2.)
    assert clocks['frequency_ratio']==two_clocks(.8,1.,2.)['frequency_ratio']==.5
    paths=serial_parallel(4)
    assert paths['serial_effective_rate']==.25 and paths['parallel_first_event_rate']==4
    d=diamond(5,3,100)
    assert d['proper_time_imported']==4 and d['expected_event_count']==800
    assert math.sqrt(2*800/400)==2 # same count, different assumed density
    return {'status':'PASS: conditional known physics and illustrative algebra; NO new Omega law',
        'null_timelike_comparison':factors,
        'same_massless_speed_different_omega':{'mode_1':massless_1,'mode_2':massless_2},
        'massive_mode_same_limit':massive,
        'quantum_speed_limit_seconds_by_delta_E_eV':bounds,
        'lattice_not_exact_Lorentz':lattice_cases,
        'common_geometry_two_ideal_clocks':clocks,
        'serial_vs_parallel_kinetics':paths,
        'causal_diamond_metric_and_density_imported':d,
        'negative_results':[
            'Null proper time does not define an update rate or a photon rest frame',
            'c is a propagation speed, not an update frequency',
            'Gap, stability, internal frequency, and gravitational dilation are distinct',
            'A rise in local reaction rate does not speed up proper time',
            'A common clock lapse cancels in colocated ideal clock ratios',
            'Finite-grid group speeds differ and do not prove exact Lorentz symmetry',
            'Causal interval event counts require metric/density and cannot fix seconds alone']}

if __name__=='__main__': print(json.dumps(run(),ensure_ascii=False,indent=2))
