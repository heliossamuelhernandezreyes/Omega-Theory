#!/usr/bin/env python3
"""Omega R16: identifiability of dynamics and inertial BAND mass.

Exploratory countermodels: bound identity on Z (or finite cyclic approximation),
unitary nearest-neighbor Hamiltonians with J>0, fixed internal clock frequency,
and stochastic walks with identical allowed adjacency. None of the Hamiltonian,
Hilbert structure, the clock, hbar, lattice spacing, or J follows from Omega.
"""
from __future__ import annotations

import argparse
import cmath
import csv
import json
import math
from pathlib import Path


def pos(name: str, value: float) -> None:
    if not isinstance(value,(int,float)) or not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")


def band_energy(J: float, wave_number: float, a: float=1.0, E0: float=0.0) -> float:
    pos('J',J); pos('a',a)
    if not math.isfinite(wave_number) or not math.isfinite(E0): raise ValueError('invalid wave number or offset')
    return E0-2*J*math.cos(a*wave_number)


def band_velocity(J: float, wave_number: float, a: float=1.0,hbar: float=1.0) -> float:
    pos('J',J);pos('a',a);pos('hbar',hbar)
    return 2*J*a*math.sin(a*wave_number)/hbar


def inertial_band_mass(J: float,a:float=1.0,hbar:float=1.0) -> float:
    pos('J',J);pos('a',a);pos('hbar',hbar)
    return hbar*hbar/(2*J*a*a)


def dimensionless_clock_ratio(J:float,omega:float=1.0,hbar:float=1.0) -> float:
    """Bandwidth over a FIXED reference clock energy hbar*omega."""
    pos('J',J);pos('omega',omega);pos('hbar',hbar)
    return 4*J/(hbar*omega)


def dimer_retained_q(phase:int=0) -> tuple[float,float]:
    """Same conserved auxiliary q within each translated identity, not energy."""
    if phase == 0: return (1.6,0.4)
    if phase == 1: return (0.4,1.6)
    raise ValueError('phase must be 0 or 1')


def allowed_edges(N:int) -> set[tuple[int,int]]:
    if not isinstance(N,int) or N < 5:raise ValueError('N >= 5')
    return {(i,(i+1)%N) for i in range(N)} | {(i,(i-1)%N) for i in range(N)}


def hamiltonian_ring(N:int,J:float,E0:float=0.0)->list[list[float]]:
    pos('J',J)
    if N < 5 or not isinstance(N,int):raise ValueError('N >= 5')
    H=[[float(E0) if i==j else 0.0 for j in range(N)] for i in range(N)]
    for x,y in allowed_edges(N):H[x][y]=-J
    return H


def two_sector_hamiltonian_ring(N:int,J:float,gap:float=4.0)->list[list[float]]:
    """A fixed B--F spectral offset, no identity leakage, common kinetic scale.

    Basis |n,B> and |n,F>, same adjacency inside each sector; off-block
    elements identically zero. Each k has E_F(k)-E_B(k)=gap for every J.
    This stability is POSTULATED by block diagonality, not derived.
    """
    pos('gap',gap)
    b=hamiltonian_ring(N,J)
    f=hamiltonian_ring(N,J,gap)
    Z=[[0.0]*N for _ in range(N)]
    return [b[i]+Z[i] for i in range(N)]+[Z[i]+f[i] for i in range(N)]


def jacobi_eigenvalues_symmetric(M:list[list[float]], tolerance:float=1e-13) -> list[float]:
    """Independent real symmetric eigenvalues via rotations; no numpy needed."""
    n=len(M)
    if n < 2 or any(len(row)!=n for row in M):raise ValueError('not square')
    A=[list(row) for row in M]
    for _ in range(100*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(A[ij[0]][ij[1]]))
        apq=A[p][q]
        if abs(apq)<tolerance:break
        tau=(A[q][q]-A[p][p])/(2*apq)
        t=(1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau))
        c=1/math.sqrt(1+t*t)
        s=t*c
        app=A[p][p];aqq=A[q][q]
        A[p][p]=app-t*apq
        A[q][q]=aqq+t*apq
        A[p][q]=A[q][p]=0.0
        for z in range(n):
            if z!=p and z!=q:
                azp,azq=A[z][p],A[z][q]
                A[z][p]=A[p][z]=c*azp-s*azq
                A[z][q]=A[q][z]=s*azp+c*azq
    else: raise RuntimeError('Jacobi nonconvergence')
    return sorted(A[i][i] for i in range(n))


def ring_analytic_spectrum(N:int,J:float,E0:float=0.0)->list[float]:
    if N<5:raise ValueError('N >= 5')
    return sorted(band_energy(J,2*math.pi*k/N,E0=E0) for k in range(N))


def evolved_localized_amplitudes(N:int,J:float,t:float,hbar:float=1.0)->list[complex]:
    """Exact Fourier propagation of delta site 0 on a ring."""
    pos('J',J);pos('hbar',hbar)
    if not isinstance(N,int) or N<5:raise ValueError('N>=5')
    if not math.isfinite(t):raise ValueError('invalid t')
    return [sum(cmath.exp(1j*(2*math.pi*k*x/N-band_energy(J,2*math.pi*k/N)*t/hbar))
                for k in range(N))/N for x in range(N)]


def prob_total(psi:list[complex])->float:
    return sum(abs(a)**2 for a in psi)


def stochastic_eigenvalue(r:float,k:float,a:float=1.0)->float:
    """Symmetric CTMC: jump rate r to each neighbor, infinite lattice."""
    pos('r',r);pos('a',a)
    return -2*r*(1-math.cos(k*a))


def stochastic_D(r:float,a:float=1.0)->float:
    pos('r',r);pos('a',a)
    return r*a*a


def second_difference_curvature(J:float,a:float=1.0,h:float=1e-3)->float:
    pos('h',h)
    return (band_energy(J,h,a)-2*band_energy(J,0,a)+band_energy(J,-h,a))/(h*h)


def run()->dict:
    omega=1.0;hbar=1.0;a=1.0
    rows=[]
    for J in (0.25,0.5,1.0,2.0,4.0):
        H=hamiltonian_ring(11,J)
        ev=jacobi_eigenvalues_symmetric(H)
        an=ring_analytic_spectrum(11,J)
        diff=max(abs(x-y) for x,y in zip(ev,an))
        norm_errors=[abs(prob_total(evolved_localized_amplitudes(11,J,t))-1) for t in (0,0.1,0.7,2.3,5)]
        rows.append({'J':J,'clock_frequency':omega,'binding_identity':'B','A_candidate':'same unspecified A',
                     'hbar':hbar,'lattice_spacing':a,'mass_band':inertial_band_mass(J),
                     'bandwidth_clock_ratio':dimensionless_clock_ratio(J,omega,hbar),
                     'band_velocity_k_pi4':band_velocity(J,math.pi/4),
                     'max_eigenvalue_error':diff,'max_norm_error':max(norm_errors),
                     'band_curvature_numeric':second_difference_curvature(J),
                     'fixed_binding_gap_by_k':4.0,
                     'two_sector_spectrum_numeric_max_error':max(abs(a-b) for a,b in zip(
                       jacobi_eigenvalues_symmetric(two_sector_hamiltonian_ring(7,J,4.0)),
                       sorted(ring_analytic_spectrum(7,J)+[x+4.0 for x in ring_analytic_spectrum(7,J)])))})
    return {
        'study':'Omega R16 - does shared identity select inertial dynamics?',
        'status':'EXPLORATORY, NO-GO (conditional), NOT CANON; NO derivation of fundamental inertia',
        'hypotheses_imported':['Hilbert space of bound-center positions','unitary Schrodinger time evolution',
         'real nearest-neighbor translation-invariant Hamiltonian J','lattice metric a',
         'external fixed clock omega','hbar and time coordinates','Born probability rule'],
        'same_constraints_for_all_J':['same Γ nearest neighbor graph','same fixed bound identity sector B',
         'same auxiliary conserved q=2','same fixed B--F energy gap Δ=4 per k (imported)','same translation and reflection symmetry',
         'same positive and reversible unitary evolution','same reference clock omega'],
        'counterexamples':rows,
        'contrasting_classical_dynamics':{'r':1.0,'q_total':2.0,'same_adjacency':True,
                                         'classical_D':stochastic_D(1.0),
                                         'no_ballistic_inertial_mass':'diffusion, not F=ma'},
        'no_go':'Identical identity and continuation support, with fixed clock, allow distinct bandwidth/clock ratios and effective masses. A selecting law is missing.',
        'physical_claims_not_established':['No electron/proton rest mass derived','No mass-energy relation derived',
           'No time or length metric derived','No relativistic causal speed derived',
           'No universal gravitational coupling or lensing derived','No probability measure selected from Γ',
           'No mapping from A to J or environmental source field derived']}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=Path('research/data'))
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    data=run()
    (args.out/'OMEGA_R16_SELECCION_DINAMICA_RESULTADOS.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    with (args.out/'OMEGA_R16_MASA_RELOJ.csv').open('w',newline='',encoding='utf-8') as f:
        fields=['J','clock_frequency','mass_band','bandwidth_clock_ratio','band_velocity_k_pi4','max_eigenvalue_error','max_norm_error','band_curvature_numeric','two_sector_spectrum_numeric_max_error'];w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data['counterexamples'])
    return data

if __name__=='__main__':
    d=main()
    print(f"R16 complete: {len(d['counterexamples'])} countermodels, status {d['status']}")
