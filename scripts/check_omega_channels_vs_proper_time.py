#!/usr/bin/env python3
"""Omega: canales de reaccion por tiempo propio vs ritmo de reloj exterior.

VERIFICA una consecuencia algebraica de GR y un modelo arbitrario de canales;
NO simula el interior ni el acrecimiento real de un agujero negro.
"""
from __future__ import annotations

import json
import math

G = 6.67430e-11
C = 299792458.0
M_SUN = 1.98847e30


def schwarzschild_radius(mass_solar: float) -> float:
    if not (math.isfinite(mass_solar) and mass_solar > 0):
        raise ValueError("mass_solar must be positive and finite")
    return 2 * G * M_SUN * mass_solar / C ** 2


def lapse_static_exterior(mass_solar: float, radius_m: float) -> float:
    rs = schwarzschild_radius(mass_solar)
    if not (math.isfinite(radius_m) and radius_m > rs):
        raise ValueError("static clock must be exterior to the horizon")
    return math.sqrt(1 - rs / radius_m)


def channel_total_rate(*rates_per_proper_second: float) -> float:
    if not rates_per_proper_second or any(
        not math.isfinite(x) or x < 0 for x in rates_per_proper_second
    ):
        raise ValueError("channels must have finite nonnegative rates")
    return sum(rates_per_proper_second)


def counts_per_asymptotic_second(
    local_rate: float, alpha: float, escape_fraction: float = 1.0
) -> float:
    if not (local_rate >= 0 and 0 < alpha <= 1 and 0 <= escape_fraction <= 1):
        raise ValueError("invalid local rate, lapse or escape fraction")
    return local_rate * alpha * escape_fraction


def fraction_transformed(local_rate: float, proper_duration_s: float) -> float:
    if local_rate < 0 or proper_duration_s < 0:
        raise ValueError("parameters must be nonnegative")
    return -math.expm1(-local_rate * proper_duration_s)


def run_checks() -> dict:
    m0, m1 = 20.0, 25.0
    # Fixed areal radius, exterior in BOTH static end states.
    r = 2 * schwarzschild_radius(m0)
    alpha0 = lapse_static_exterior(m0, r)
    alpha1 = lapse_static_exterior(m1, r)
    assert math.isclose(alpha0, math.sqrt(0.5), rel_tol=1e-12)
    assert math.isclose(alpha1, math.sqrt(0.375), rel_tol=1e-12)
    assert alpha1 < alpha0

    base_rate = 1.0  # UNIDADES ARBITRARIAS, no tasa QED predicha.
    base_observed = counts_per_asymptotic_second(base_rate, alpha0)
    threshold = alpha0 / alpha1
    rows = []
    for additional_channel in (0.0, 0.1, 0.2, 0.5, 1.0):
        local_rate = channel_total_rate(base_rate, additional_channel)
        observed = counts_per_asymptotic_second(local_rate, alpha1)
        rows.append({
            "additional_local_channel_per_s": additional_channel,
            "total_events_per_proper_s": local_rate,
            "signal_events_per_distant_s_if_all_escape": round(observed, 9),
            "observed_rate_divided_by_initial": round(observed / base_observed, 9),
            "transformed_fraction_after_1_proper_s": round(
                fraction_transformed(local_rate, 1), 9
            )
        })

    assert rows[1]["observed_rate_divided_by_initial"] < 1
    assert rows[2]["observed_rate_divided_by_initial"] > 1
    assert math.isclose(threshold, math.sqrt(4 / 3), rel_tol=1e-12)
    assert math.isclose(fraction_transformed(1.5, 1), 1 - math.exp(-1.5))
    assert counts_per_asymptotic_second(1.5, alpha1, 0.0) == 0

    try:
        lapse_static_exterior(m1, schwarzschild_radius(m1))
        raise AssertionError("no stationary clock on the horizon")
    except ValueError:
        pass

    return {
        "status": "PASS: conditional algebra, NOT a validation of Omega",
        "initial_mass_solar": m0,
        "final_mass_solar": m1,
        "fixed_areal_radius_m": round(r, 6),
        "clock_lapse_before": round(alpha0, 9),
        "clock_lapse_after": round(alpha1, 9),
        "clock_lapse_after_over_before": round(alpha1 / alpha0, 9),
        "local_rate_factor_to_increase_received_signal_rate": round(threshold, 9),
        "base_local_rate_per_proper_s": base_rate,
        "base_signal_rate_if_all_escape": round(base_observed, 9),
        "cases": rows,
        "limitations": [
            "Two separate static Schwarzschild EXTERIOR end states only",
            "The mass increment of 25 percent is highly dynamical in reality",
            "Channel rates are toy inputs: no annihilation cross-section computed",
            "Outgoing observable radial signal assumed for every event",
            "At or inside horizon no classic signal reaches distant infinity",
            "A rise in reactions per proper time is not an acceleration of time",
            "No mapping from Omega r_e to measured seconds or GR derived"
        ]
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), ensure_ascii=False, indent=2))
