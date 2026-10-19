#!/usr/bin/env python3
"""Antimateria: cargas conservadas y umbral de dos fotones.

Solo reproduce condiciones CINEMATICAS de relatividad/QFT. No valida Omega.
"""
from __future__ import annotations
import json
import math

ELECTRON_REST_MEV = 0.51099895069
PAIR_THRESHOLD_MEV = 2 * ELECTRON_REST_MEV


def two_photon_invariant_mev(e1: float, e2: float, angle_degrees: float) -> float:
    if not (math.isfinite(e1) and math.isfinite(e2) and e1 >= 0 and e2 >= 0):
        raise ValueError("Photon energies must be finite and nonnegative")
    if not (math.isfinite(angle_degrees) and 0 <= angle_degrees <= 180):
        raise ValueError("Relative angle must be 0..180 degrees")
    theta = math.radians(angle_degrees)
    return math.sqrt(max(0.0, 2 * e1 * e2 * (1 - math.cos(theta))))


# (charge / |e|, baryon number, electron-family lepton number).
# Quantum numbers are not "potentiality"; weak interactions constrain other numbers.
NUMBERS = {
    "electron": (-1, 0, 1), "positron": (1, 0, -1),
    "photon": (0, 0, 0), "proton": (1, 1, 0),
    "antiproton": (-1, -1, 0), "neutron": (0, 1, 0),
    "nu_e": (0, 0, 1),
}


def totals(species: tuple[str, ...]) -> tuple[int, ...]:
    return tuple(sum(NUMBERS[name][i] for name in species) for i in range(3))


def run_checks() -> dict:
    out = []
    for angle in (0, 90, 180):
        w = two_photon_invariant_mev(.6, .6, angle)
        out.append({
            "angle_degrees": angle,
            "photon_total_energy_mev": 1.2,
            "invariant_energy_mev": round(w, 9),
            "pair_creation_kinematically_allowed": w >= PAIR_THRESHOLD_MEV,
        })
    assert not out[0]["pair_creation_kinematically_allowed"]
    assert not out[1]["pair_creation_kinematically_allowed"]
    assert out[2]["pair_creation_kinematically_allowed"]
    assert math.isclose(out[0]["invariant_energy_mev"], 0.0, abs_tol=1e-12)
    assert math.isclose(out[2]["invariant_energy_mev"], 1.2, abs_tol=1e-9)
    assert totals(("electron", "positron")) == totals(("photon", "photon"))
    assert totals(("photon", "photon")) == (0, 0, 0)
    assert totals(("proton",)) == totals(("neutron", "positron", "nu_e"))
    assert totals(("proton", "antiproton")) == (0, 0, 0)

    return {
        "status": "PASS: known kinematic/charge balances only; Omega NOT tested",
        "electron_rest_mev": ELECTRON_REST_MEV,
        "pair_threshold_mev": round(PAIR_THRESHOLD_MEV, 9),
        "two_photon_example": out,
        "rest_annihilation_photons_mev_each": ELECTRON_REST_MEV,
        "charges_preserved_in_pair_creation_annihilation_and_beta_plus": True,
        "limitations": [
            "Conservation and thresholds alone do not give transition probabilities",
            "Free isolated proton beta-plus decay is energetically forbidden",
            "Interactions and lifetimes require dynamics not included here",
            "No mapping from Omega relational potentiality to physical charge was derived",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), ensure_ascii=False, indent=2))
