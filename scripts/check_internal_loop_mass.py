#!/usr/bin/env python3
"""Chequeo exploratorio: dos canales propagantes acoplados.

NO prueba que Omega derive masa; reproduce identidades del modelo Dirac 1+1
H = v*p*sigma_z + g*sigma_x, en unidades operacionales arbitrarias.
"""
from __future__ import annotations
import json
import math


def positive_energy(p: float, v: float, g: float) -> float:
    if not (v > 0 and g >= 0):
        raise ValueError("v>0 y g>=0")
    return math.hypot(v * p, g)


def net_velocity(p: float, v: float, g: float) -> float:
    e = positive_energy(p, v, g)
    if e == 0:
        raise ValueError("En p=g=0 hay degeneracion y no una rama diferenciable")
    return v * v * p / e


def run_checks() -> dict:
    p, v = 1.0, 1.0
    gs = [0.0, 0.25, 0.5, 1.0, 2.0, 4.0]
    samples = []
    for g in gs:
        e = positive_energy(p, v, g)
        velocity = net_velocity(p, v, g)
        # Tr H=0; det H=-(v*p)^2-g^2: los autovalores son +/-E.
        assert abs(e * e - ((v * p)**2 + g * g)) < 1e-12
        # Derivada numerica independiente de la formula analitica.
        h = 1e-5
        finite_difference = (
            positive_energy(p + h, v, g) - positive_energy(p - h, v, g)
        ) / (2 * h)
        assert math.isclose(velocity, finite_difference, abs_tol=2e-10)
        assert abs(velocity) <= v + 1e-12
        samples.append({
            "g_over_vp": g / (v * p),
            "positive_energy_over_vp": round(e / (v * p), 9),
            "group_velocity_over_v": round(velocity / v, 9),
        })

    assert net_velocity(0, v, 1.0) == 0
    assert math.isclose(positive_energy(0, v, 1.0), 1.0)
    assert math.isclose(net_velocity(p, v, 0), v)
    assert net_velocity(1e6, v, 1.0) < v

    return {
        "status": "PASS: solo consistencia del modelo importado, NO validacion de Omega",
        "model": "1+1 Dirac; H=v*p*sigma_z+g*sigma_x",
        "units": "v=p=1; g energia arbitraria",
        "results": samples,
        "negative_findings": [
            "g no se deriva de la geometria Omega",
            "la masa no se crea por intentar exceder la velocidad limite",
            "el mecanismo no predice gravedad ni la estabilidad nuclear",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), ensure_ascii=False, indent=2))
