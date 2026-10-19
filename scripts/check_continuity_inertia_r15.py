#!/usr/bin/env python3
"""Omega R15: two independent toy models, no derivation of fundamental mass.

A. Classical sequential-gate walker: internal coordination limits mobility.
B. Imported 1D attractive lattice quantum pair: binding and effective band mass.

No mapping from potentiality/asfixia to model couplings is supplied or implied.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path


def _positive(*values: float) -> None:
    if any((not math.isfinite(v)) or v <= 0 for v in values):
        raise ValueError("Parameters must be finite and strictly positive")


def retained_q_distribution(gate: int, total: float = 2.0) -> tuple[float,float]:
    """Auxiliary redistribution of q, not identification with physical energy.

    The same total is retained in both coordination phases. Translations carry
    the pair along, with the same aggregate q. This is a chosen model rule.
    """
    _positive(total)
    if gate not in (0,1):
        raise ValueError("gate must be 0 or 1")
    return (0.9*total,0.1*total) if gate==0 else (0.1*total,0.9*total)


def free_diffusion(r: float, a: float = 1.0) -> float:
    """Symmetric nearest-neighbour random walk, jump rate r in total."""
    _positive(r, a)
    return a*a*r/2.0


def coordinated_diffusion(k: float, r: float, a: float = 1.0) -> float:
    """One move requires serial Exp(k) 'prepare' and Exp(r) 'release' stages.

    A release goes to +a or -a with equal probability; no individual
    constituent is represented as an independently freely moving particle.
    Classical long-time transport coefficient, not inertial mass.
    """
    _positive(k, r, a)
    return 0.5*a*a*(k*r/(k+r))


def coordinated_velocity(k: float, r: float, bias: float, a: float = 1.0) -> float:
    """Stationary signed drift after a dimensionless directional bias.

    bias is an external dimensionless parameter, not a physical force.
    """
    _positive(k, r, a)
    if not math.isfinite(bias):
        raise ValueError("Bias must be finite")
    return a*(k*r/(k+r))*math.tanh(bias/2.0)


def bound_energy(U: float, J: float, K: float) -> float:
    """Exact isolated on-site attractive dimer band, 1D infinite lattice.

    Hamiltonian and Born/Hilbert structure are IMPORTED, not from Omega.
    K is dimensionless crystal momentum K*a and hbar=a=1 when computing mass.
    """
    _positive(U, J)
    if not math.isfinite(K):
        raise ValueError("K must be finite")
    return -math.hypot(U, 4*J*math.cos(K/2.0))


def scattering_minimum(J: float, K: float) -> float:
    _positive(J)
    if not math.isfinite(K):
        raise ValueError("K must be finite")
    return -4*J*abs(math.cos(K/2.0))


def binding_gap(U: float, J: float, K: float) -> float:
    """Positive gap separating bound energy below scattering continuum."""
    return scattering_minimum(J, K)-bound_energy(U,J,K)


def coincident_separation_probability(U: float, J: float, K: float) -> float:
    """Probability for lattice relative separation r=0 in a normalized eigenstate."""
    _positive(U, J)
    if not math.isfinite(K):
        raise ValueError("K must be finite")
    return U/math.hypot(U, 4*J*math.cos(K/2.0))


def pair_mass(U: float, J: float, lattice_spacing: float = 1.0, hbar: float = 1.0) -> float:
    """Effective positive band mass at K=0 for attractively bound pair.

    Not a relativistic rest mass; units hbar^2/(energy*length^2).
    """
    _positive(U, J, lattice_spacing, hbar)
    return hbar*hbar*math.hypot(U, 4*J)/(4*J*J*lattice_spacing*lattice_spacing)


def free_pair_mass(J: float, lattice_spacing: float = 1.0, hbar: float = 1.0) -> float:
    """Sum of two separate-particle band masses near individual k=0."""
    _positive(J, lattice_spacing, hbar)
    return hbar*hbar/(J*lattice_spacing*lattice_spacing)


def relative_mass_ratio(U: float, J: float) -> float:
    _positive(U, J)
    return math.hypot(U, 4*J)/(4*J)


def numerical_lowest_tridiagonal_eigenvalue(U: float, J: float, K: float, half_width: int = 100) -> float:
    """Independent finite-difference diagonalization using Sturm bisection.

    Relative-coordinate Hamiltonian r=-L,...,+L; onsite -U at r=0;
    off-diagonal hopping -T, T=2J cos(K/2).
    Eigenvalue tends to bound_energy as L->infinity for U>0.
    """
    _positive(U, J)
    if not isinstance(half_width, int) or half_width < 2:
        raise ValueError("half_width must be an int >= 2")
    if not math.isfinite(K):
        raise ValueError("K must be finite")
    offsq = (2*J*math.cos(K/2.0))**2
    N = 2*half_width+1

    def count_below(x: float) -> int:
        d = -x
        cnt = int(d < 0)
        for i in range(1, N):
            if abs(d) < 1e-14:
                d = -1e-14 if d < 0 else 1e-14
            diag = -U if i == half_width else 0.0
            d = diag-x-offsq/d
            cnt += int(d < 0)
        return cnt

    low = -U-4*J-1.0
    high = 1.0
    if count_below(low)!=0 or count_below(high)<1:
        raise ArithmeticError("Failed to bracket the lowest eigenvalue")
    for _ in range(78):
        mid = (low+high)/2
        if count_below(mid):
            high=mid
        else:
            low=mid
    return (low+high)/2


def numeric_band_curvature(U: float, J: float, delta: float = 1e-3) -> float:
    """Finite-difference E''(K) at 0, with K dimensionless."""
    _positive(U, J, delta)
    return (bound_energy(U,J,delta)-2*bound_energy(U,J,0)+bound_energy(U,J,-delta))/delta**2


def run() -> dict:
    classical=[]
    r=1.0
    for k in (0.2, 1.0, 5.0, 50.0):
        d=coordinated_diffusion(k,r)
        classical.append({"k":k,"r":r,"D_free":free_diffusion(r),"D_pair":d,
                          "mobility_ratio":d/free_diffusion(r),
                          "bias_susceptibility":coordinated_velocity(k,r,1e-5)/1e-5})
    quantum=[]
    for U in (0.5,1.0,2.0,4.0,8.0,12.0):
        J=1.0
        quantum.append({"U":U,"J":J,"K":0.0,"bound_energy":bound_energy(U,J,0),
                        "gap":binding_gap(U,J,0),
                        "prob_same_site":coincident_separation_probability(U,J,0),
                        "effective_mass_hbar_a_1":pair_mass(U,J),
                        "mass_ratio_to_two_free":relative_mass_ratio(U,J),
                        "tridiagonal_eigenvalue_L100":numerical_lowest_tridiagonal_eigenvalue(U,J,0),
                        "finite_diff_curvature":numeric_band_curvature(U,J)})
    equal_geometry=[]
    for J in (0.5, 1.0, 2.0):
        U=4*J
        equal_geometry.append({"J":J,"U":U,
                         "prob_same_site":coincident_separation_probability(U,J,0),
                         "effective_mass_hbar_a_1":pair_mass(U,J),
                         "gap":binding_gap(U,J,0)})
    return {"study":"Omega R15 — compatibility, binding, mobility and effective mass",
            "status":"EXPLORATORY / NO CANON / NOT PHYSICAL VALIDATION",
            "classical":classical,"q_distribution_by_gate":{"0":list(retained_q_distribution(0)),"1":list(retained_q_distribution(1))},"quantum_imported":quantum,
            "same_dimensionless_binding_different_mass":equal_geometry,
            "limits":["A compatibility graph plus conservation does not select transition rates.",
                      "Classical mobility (D or drift) is not inertial mass or Newtonian acceleration.",
                      "The lattice quantum model imports Hilbert dynamics, J, U, a and hbar.",
                      "The index U/J is NOT ontological asfixia A.",
                      "A two-body closed scattering state cannot release binding energy into nowhere; capture needs another channel or preparation.",
                      "Neither photon-to-matter creation nor gravity is derived; light itself can gravitate.",
                      "An external evolution clock is used by both toy models; time is not emergent.",
                      "Quantum norm conservation is not conservation of a physical potentiality fluid."]}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--out", default="research/data")
    args=parser.parse_args()
    out=Path(args.out)
    out.mkdir(parents=True,exist_ok=True)
    res=run()
    (out/"OMEGA_R15_INERCIA_RESULTADOS.json").write_text(json.dumps(res,indent=2,ensure_ascii=False,allow_nan=False)+"\n",encoding="utf-8")
    for filename, key in (("OMEGA_R15_MOVILIDAD.csv","classical"),
                           ("OMEGA_R15_PAR_CUANTICO.csv","quantum_imported"),
                           ("OMEGA_R15_IDENTIFICABILIDAD.csv","same_dimensionless_binding_different_mass")):
        with (out/filename).open("w",newline="",encoding="utf-8") as f:
            rows=res[key]
            writer=csv.DictWriter(f,fieldnames=list(rows[0]))
            writer.writeheader();writer.writerows(rows)
    print(json.dumps({"classical_rows":len(res["classical"]),
                      "quantum_rows":len(res["quantum_imported"]),
                      "identifiability_rows":len(res["same_dimensionless_binding_different_mass"])},indent=2))


if __name__=="__main__":
    main()
