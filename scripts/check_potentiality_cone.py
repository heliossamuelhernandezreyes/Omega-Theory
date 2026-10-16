#!/usr/bin/env python3
"""Prototipo exploratorio de Omega: cono de velocidades de grupo y brechas.

NO deriva Lorentz, gravedad, masa física, ni la velocidad experimental c.
Se ejecuta con Python estándar:
    python scripts/check_potentiality_cone.py
"""
from __future__ import annotations

import json
import math


def omega(k: float, a: float, v_star: float, gap: float) -> float:
    """Dispersion de cadena local: omega^2=gap^2+4(v/a)^2 sin^2(ka/2)."""
    if not (a > 0 and v_star > 0 and gap >= 0):
        raise ValueError("Se requiere a>0, v_star>0 y gap>=0")
    if not math.isfinite(k):
        raise ValueError("k debe ser finito")
    return math.hypot(gap, 2.0 * v_star / a * math.sin(k * a / 2.0))


def group_speed(k: float, a: float, v_star: float, gap: float) -> float:
    """Derivada de omega(k); en k=0, gap=0 se usa el limite por la derecha."""
    w = omega(k, a, v_star, gap)
    if w == 0.0:
        return v_star
    return (v_star * v_star / (a * w)) * math.sin(k * a)


def branching(weights: list[float]) -> list[float]:
    if not weights or any((not math.isfinite(w) or w <= 0) for w in weights):
        raise ValueError("Todos los pesos deben ser positivos y finitos")
    return [w / sum(weights) for w in weights]


def run_checks() -> dict[str, object]:
    a, v = 1.0, 1.0  # UNIDADES ARBITRARIAS; NO se identifica con c.
    ks = [math.pi * i / (400 * a) for i in range(401)]
    gaps = [0.0, 0.5, 1.0, 2.0]
    all_speeds = [abs(group_speed(k, a, v, gap))
                  for gap in gaps for k in ks]
    max_speed = max(all_speeds)
    assert max_speed <= v + 1e-12

    # En la rama gapless, la pendiente por la derecha en k=0 es v.
    assert math.isclose(group_speed(0.0, a, v, 0.0), v, abs_tol=1e-12)
    # En la rama gapped, la velocidad de grupo es cero en k=0.
    assert all(group_speed(0.0, a, v, g) == 0 for g in gaps[1:])

    # Aproximacion continua: omega^2 = gap^2 + v^2 k^2 + O(a^2 k^4).
    small_ka = 0.1
    residual = ((omega(small_ka / a, a, v, 0.5) ** 2 - 0.5 ** 2)
                / (v * v * (small_ka / a) ** 2) - 1.0)
    assert abs(residual) < 0.001

    # Contraejemplo: la malla NO obedece dispersion de Lorentz exactamente.
    large_ka = 1.0
    rel_discrepancy = ((omega(large_ka / a, a, v, 0.0) ** 2)
                       / (v * v * (large_ka / a) ** 2) - 1.0)
    assert abs(rel_discrepancy) > 0.08

    # Un factor comun en tasas conserva la ramificacion, no fija relojes.
    base = [0.2, 0.4, 1.0]
    scaled = [w * 7.5 for w in base]
    assert all(math.isclose(x, y, rel_tol=1e-14)
               for x, y in zip(branching(base), branching(scaled)))

    # El mismo gap puede coexistir con diferentes tasas de desintegracion.
    # Gamma es un parametro INDEPENDIENTE de este modelo conservativo.
    same_gap_different_decay = [dict(gap=0.5, decay=0.0),
                                dict(gap=0.5, decay=0.1)]
    assert same_gap_different_decay[0]["gap"] == same_gap_different_decay[1]["gap"]

    return {
        "status": "PASS: verificaciones internas del modelo, NO validacion fisica",
        "units": "a=v_star=1; gap en unidades arbitrarias",
        "sampled_k_points_per_gap": len(ks),
        "gaps": gaps,
        "max_abs_group_speed": max_speed,
        "speed_bound": v,
        "small_ka": small_ka,
        "small_ka_relative_omega_sq_error": residual,
        "large_ka": large_ka,
        "large_ka_relative_omega_sq_error": rel_discrepancy,
        "branching_invariant_under_common_scale": True,
        "gap_does_not_determine_decay": True,
        "not_tested": [
            "velocidad causal de frente de onda",
            "invariancia Lorentz exacta",
            "relacion fundamental entre r_e y acoplamientos J,K",
            "principio de equivalencia",
            "gravedad dinamica o pruebas observacionales",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, ensure_ascii=False))
