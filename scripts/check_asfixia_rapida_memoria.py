#!/usr/bin/env python3
"""Modelo conceptual de asfixia rápida, en unidades arbitrarias.

x' = -(k_floor + k0 exp(-t/tq))*x, x(0)=x0.
x es una desviación estructural, NO masa. No simula colapso gravitatorio.
"""
import math
import json


def remanence(t, tq, k0=1.0, k_floor=0.0, x0=1.0):
    if t < 0 or tq <= 0 or k0 < 0 or k_floor < 0:
        raise ValueError("invalid nonnegative parameters")
    return x0 * math.exp(-k_floor*t-k0*tq*(-math.expm1(-t/tq)))


def test():
    assert math.isclose(remanence(0, 1), 1)
    assert math.isclose(remanence(100, .1), math.exp(-.1), rel_tol=1e-12)
    assert math.isclose(remanence(100, 10), math.exp(-10*(1-math.exp(-10))),
                        rel_tol=1e-12)
    assert remanence(100, .1) > remanence(100, 10)
    assert remanence(100, .1, k_floor=.002) < remanence(100, .1)
    rows = []
    for tq in (.1, .5, 1, 3, 10):
        x = remanence(100, tq)
        rows.append({
            "tiempo_cierre": tq,
            "remanencia_x": round(x, 8),
            "proxy_energia_0_5_x2": round(.5*x*x, 8),
        })
    return {"resultado": "PASS: comprobaciones internas del modelo, NO evidencia física",
            "parametros": {"k0": 1, "k_floor": 0, "t": 100,
                            "unidades": "arbitrarias"},
            "resultados": rows,
            "negativos": [
                "remanencia no es masa física derivada",
                "si k_floor>0, x tiende a cero cuando t tiende a infinito",
                "modelo no describe templado microestructural detallado ni agujeros negros",
            ]}


if __name__ == "__main__":
    print(json.dumps(test(), ensure_ascii=False, indent=2))
