#!/usr/bin/env python3
"""Modelo auxiliar phi^4 de "cicatriz" con energía residual.
No deriva espacio, tiempo, masa física ni física nueva desde Omega.
"""
from __future__ import annotations
import json
import math


def ell0(kap=1., lam=1., v=1.):
    return math.sqrt(2*kap/(lam*v*v))


def kink_energy(kap=1., lam=1., v=1.):
    return 2*math.sqrt(2)/3*v**3*math.sqrt(kap*lam)


def energy(ell, kap=1., lam=1., v=1.):
    if min(ell, kap, lam, v) <= 0:
        raise ValueError("ell, kap, lam, v deben ser positivos")
    return 2*kap*v*v/(3*ell) + lam*v**4*ell/3


def numerical_energy(ell, kap=1., lam=1., v=1.):
    L = 20*max(ell, ell0(kap, lam, v))
    n = 20000
    dx = 2*L/n
    total = 0.
    for i in range(n):
        x = -L+(i+0.5)*dx
        z = 1/math.cosh(x/ell)**2
        total += dx*(kap/2*(v/ell*z)**2 + lam/4*(v*v*z)**2)
    return total


def run_checks():
    w, E0 = ell0(), kink_energy()
    assert math.isclose(energy(w), E0, rel_tol=1e-13)
    assert math.isclose(numerical_energy(w), E0, rel_tol=1e-6)
    rows=[]
    for r in (.25,.5,1.,2.,4.):
        Ei=energy(r*w)
        assert math.isclose(numerical_energy(r*w), Ei, rel_tol=1e-6)
        assert Ei >= E0-1e-12
        rows.append({
            "initial_width_ratio":r,
            "initial_energy":round(Ei,9),
            "minimum_retained_energy":round(E0,9),
            "energy_to_export_on_relaxation":round(Ei-E0,9),
        })
    assert rows[0]["initial_energy"] == rows[-1]["initial_energy"]
    return {
        "status":"PASS: comprobación interna, NO evidencia física",
        "units":"kappa=lambda=v=1 (arbitrarias)",
        "topological_charge":"Q=1 por las fronteras -v y +v",
        "vacuum_relative_energy":0,
        "minimum_defect_energy":round(E0,9),
        "cases":rows,
        "limitations":[
            "La topología se impuso con fronteras diferentes",
            "No hay dinámica temporal que transporte la energía excedente",
            "No deriva masa inercial ni gravitatoria ni espacio emergente",
            "El incremento de energía inicial no determina incremento de cicatriz final",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), ensure_ascii=False, indent=2))
