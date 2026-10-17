#!/usr/bin/env python3
"""Omega R5: one chosen local UNITARY quantum walk (U = shift * coin).

Conditional math from established discrete-time quantum walk models.
The external integer step and spatial lattice are input assumptions.
No derivation of proper time, c, Lorentz invariance, or physics of Omega.
"""
from __future__ import annotations
import json, math


def coin_step(up, down, angle):
    """On infinite integer lattice truncated with padding; complex amplitudes."""
    if len(up)!=len(down) or len(up)<3 or not (0<=angle<math.pi/2):
        raise ValueError('coin arrays must agree, theta in [0,pi/2)')
    c,s=math.cos(angle),math.sin(angle)
    a=[c*u-s*d for u,d in zip(up,down)]
    b=[s*u+c*d for u,d in zip(up,down)]
    up2=[0j]*len(up);dn2=[0j]*len(up)
    for i in range(len(up)):
        if i+1<len(up): up2[i+1]=a[i]
        if i-1>=0: dn2[i-1]=b[i]
    return up2,dn2


def localized_run(angle, steps=25, padding=7):
    """Single site initial state; bound by |x-x0|<=steps exactly."""
    if steps<1: raise ValueError('steps >= 1')
    radius=steps+padding
    up=[0j]*(2*radius+1);dn=[0j]*len(up)
    up[radius]=1+0j
    traces=[]
    for n in range(1,steps+1):
        up,dn=coin_step(up,dn,angle)
        p=[abs(a)**2+abs(b)**2 for a,b in zip(up,dn)]
        leaked=sum(v for j,v in enumerate(p) if abs(j-radius)>n)
        norm=sum(p)
        traces.append((n,norm,leaked,p[radius+n],p[radius-n]))
    return traces


def quasi_energy(k,theta):
    """U(k)=diag(e^(ik),e^(-ik)) C(theta), cos omega=cos(k)*cos(theta)."""
    if not (math.isfinite(k) and math.isfinite(theta) and 0<=theta<math.pi/2):
        raise ValueError('invalid k or theta')
    return math.acos(max(-1.,min(1.,math.cos(k)*math.cos(theta))))


def group_velocity(k,theta):
    """d omega/dk; null point theta=k=0 defined via right limit."""
    w=quasi_energy(k,theta)
    den=math.sin(w)
    if abs(den)<1e-12:
        return math.cos(theta) if abs(k)<1e-12 else -math.cos(theta)
    return math.cos(theta)*math.sin(k)/den


def spin_clock_probability(steps,theta):
    """At k=0 (spatially uniform state) U=C(theta): P(up)=cos^2(n theta)."""
    if steps<0: raise ValueError('steps>=0')
    return math.cos(steps*theta)**2


def continuum_extrapolation(momentum=0.7,mass=0.4):
    """Take k=p*eps, theta=m*eps, omega/eps -> sqrt(p^2+m^2).
    This IMPORTS an additional continuum scaling and band identification.
    """
    exact=math.hypot(momentum,mass)
    return [{'epsilon':eps,'omega_over_epsilon':quasi_energy(momentum*eps,mass*eps)/eps,
             'relative_error':quasi_energy(momentum*eps,mass*eps)/eps/exact-1}
            for eps in (0.5,0.2,0.1,0.05)]


def run_checks():
    rows=[]
    for theta in (0.,.15,.3,.6):
        traces=localized_run(theta)
        assert max(abs(norm-1) for _,norm,_,_,_ in traces)<2e-13
        assert max(leak for _,_,leak,_,_ in traces)==0
        vg=group_velocity(math.pi/2,theta)
        assert abs(vg-math.cos(theta))<1e-12
        rows.append({'theta':theta,'maximum_group_speed':vg,
                     'k0_eigenphase_gap':quasi_energy(0,theta),
                     'k0_spin_oscillation_period_steps':None if theta==0 else math.pi/theta,
                     'strict_cone_leakage':traces[-1][2],
                     'localized_probability_on_right_edge':traces[-1][3]})
    assert abs(spin_clock_probability(10,0)-1)<1e-14
    assert abs(spin_clock_probability(10,.3)-math.cos(3)**2)<1e-14
    # Causal cone and clock from same U, but its clock frequency is theta-dependent.
    assert rows[1]['k0_spin_oscillation_period_steps']>rows[2]['k0_spin_oscillation_period_steps']
    assert rows[1]['maximum_group_speed']>rows[2]['maximum_group_speed']
    # Exact lattice dynamics fails continuum Lorentz dispersion at finite k.
    finite=quasi_energy(1.,0.)
    assert abs(finite-1.)<1e-12 # null branch has omega=k for k in [0,pi]
    massive_k=quasi_energy(1.,.5)
    continuum_massive=math.hypot(1.,.5)
    assert abs(massive_k-continuum_massive)>0.03
    continuum=continuum_extrapolation()
    assert abs(continuum[-1]['relative_error'])<abs(continuum[0]['relative_error'])
    assert abs(continuum[-1]['relative_error'])<1e-4
    # Same U after global theta=0 has a front and no chosen k=0 coin ticks.
    # A toy 'clock period' is phase oscillation, NOT particle proper time.
    return {'status':'PASS: CONDITIONAL quantum walk mathematics; no Omega physical prediction',
            'generator':'U=S*C(theta), C=[[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]',
            'quasienergy':'cos(omega)=cos(k)*cos(theta)',
            'strict_causal_support':'|delta_x_in_cells| <= number_of_external_steps',
            'parameters':rows,
            'continuum_test':continuum,
            'lattice_massive_k1_theta05':massive_k,
            'relativistic_surrogate_k1_gap05':continuum_massive,
            'tests':{'norm_unitarity':True,'strict_support_cone':True,
                     'dispersion_consistency':True,'internal_clock_from_same_U':True,
                     'no_universal_clock_from_cone':True,'low_energy_limit_only':True},
            'negative_results':[
                'The computational update step is EXTERNAL: this is not a derivation of time from timeless ontology',
                'The lattice and the coin rotation are choices, not derived from Gamma_x',
                'One cell/step is not the observed c without deriving physical a/tau scale',
                'k=0 spin phase clock uses delocalized mode, not proper time of localized massive particle',
                'theta=0 internal polarization does not oscillate but massless field may still change phase and interact',
                'Higher theta yields slower group velocity but FASTER internal k=0 spin oscillation',
                'Different theta species have different internal clocks; gravitational universality not recovered',
                'Finite lattice has a preferred frame and finite-k deviations from exact Lorentz symmetry',
                'No QFT interactions, gravity, curved metric, observer-independent causal reconstruction',
            ]}

if __name__=='__main__': print(json.dumps(run_checks(),indent=2,ensure_ascii=False))
