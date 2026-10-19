#!/usr/bin/env python3
"""Causalidad: accesibilidad externa vs dinámica interna, y prueba Schwarzschild.

Es un contraejemplo lógico y un cálculo de GR importada. NO deriva gravedad
ni la masa de los agujeros negros a partir de la ontología Omega.
"""
from __future__ import annotations
import json
import math


G = 6.67430e-11
C_LIGHT = 299_792_458.0
SUN_MASS = 1.98847e30


def schwarzschild_radius(mass: float) -> float:
    if mass <= 0 or not math.isfinite(mass):
        raise ValueError("La masa ha de ser positiva y finita")
    return 2 * G * mass / (C_LIGHT ** 2)


def redshift_outward(radius: float, mass: float) -> float:
    """Razón de frecuencias ν_inf/ν_local, emisor estacionario R>r_s."""
    if radius <= schwarzschild_radius(mass):
        raise ValueError("No existe emisor estático regular en/sobre el horizonte")
    return math.sqrt(1.0 - schwarzschild_radius(mass) / radius)


def reachable(start: str, destination: str, edges: dict[str, tuple[str, ...]]) -> bool:
    pending, visited = [start], set()
    while pending:
        node = pending.pop()
        if node == destination:
            return True
        if node in visited:
            continue
        visited.add(node)
        pending.extend(edges.get(node, ()))
    return False


def run_checks() -> dict:
    rs = schwarzschild_radius(SUN_MASS)
    assert math.isclose(rs / 1000, 2.953339382, abs_tol=1e-6)

    ratios = [10.0, 3.0, 2.0, 1.1, 1.01]
    rows = []
    for q in ratios:
        a = redshift_outward(q * rs, SUN_MASS)
        b = 1 - 1 / q  # Flujo ideal de un haz radial estacionario: NO emisión isotrópica real.
        assert math.isclose(a * a, b, rel_tol=1e-13)
        rows.append({
            "R_over_rs": q,
            "compactness": round(1.0 / q, 9),
            "frequency_at_infinity_over_local": round(a, 9),
            "radial_beam_power_at_infinity_over_local": round(b, 9),
        })
    assert all(rows[i]["frequency_at_infinity_over_local"] >
               rows[i + 1]["frequency_at_infinity_over_local"]
               for i in range(len(rows) - 1))

    # Grafo causal sin ciclos: la zona oculta sigue actualizándose,
    # pero no alcanza el observador remoto.
    graph_open = {
        "I0": ("I1",),
        "I1": ("I2", "E0"),
        "I2": ("I3",),
        "E0": ("infinito",),
    }
    graph_closed = {
        "I0": ("I1",),
        "I1": ("I2",),
        "I2": ("I3",),
        "E0": ("infinito",),
    }
    assert reachable("I0", "infinito", graph_open)
    assert not reachable("I0", "infinito", graph_closed)
    assert reachable("I0", "I3", graph_closed)

    try:
        redshift_outward(rs, SUN_MASS)
        raise AssertionError("El horizonte no admite emisor estacionario")
    except ValueError:
        pass
    return {
        "status": "PASS: cálculos de GR y contraejemplo lógico interno; sin validación externa",
        "schwarzschild_radius_sun_km": round(rs / 1000, 6),
        "static_radial_emitter_cases": rows,
        "graph_closed": {
            "internal_successors_exist": True,
            "path_to_infinity_exists": False,
        },
        "limitations": [
            "La relación Schwarzschild incluye G, c y una métrica introducidos externamente.",
            "El cociente de potencias no es la luminosidad total de un objeto real.",
            "El grafo ilustrativo no define un horizonte observador-invariante.",
            "El interior de un agujero negro no está caracterizado observacionalmente.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), ensure_ascii=False, indent=2))
