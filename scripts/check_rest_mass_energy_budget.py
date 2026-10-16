#!/usr/bin/env python3
"""Ejemplos fisicos de balance masa-energia. NO prueban la teoria Omega."""
from __future__ import annotations
import json
import math

ELECTRON_REST_MEV = 0.51099895069
ATOMIC_MASS_UNIT_MEV = 931.49410242
DEUTERON_BINDING_MEV = 2.224566


def two_head_on_photons_invariant_energy_mev(e1: float, e2: float) -> float:
    """Invariant centre-of-momentum energy of two exactly opposite photons."""
    if e1 < 0 or e2 < 0:
        raise ValueError("Energies must be nonnegative")
    return 2 * math.sqrt(e1 * e2)


def equivalent_mass_defect_u(energy_mev: float) -> float:
    return energy_mev / ATOMIC_MASS_UNIT_MEV


def run_checks() -> dict:
    threshold = 2 * ELECTRON_REST_MEV
    cm_energy = two_head_on_photons_invariant_energy_mev(.6, .6)
    excess = cm_energy - threshold
    assert math.isclose(threshold, 1.02199790138, rel_tol=1e-12)
    assert math.isclose(cm_energy, 1.2, rel_tol=1e-12)
    assert excess > 0
    assert math.isclose(two_head_on_photons_invariant_energy_mev(.3, 1.2), 1.2)
    assert math.isclose(two_head_on_photons_invariant_energy_mev(1., 0.), 0.)
    assert math.isclose(equivalent_mass_defect_u(200.), .21470882046424627)
    assert math.isclose(equivalent_mass_defect_u(DEUTERON_BINDING_MEV), .002388169709524332)
    return {
        "status": "PASS: known mass-energy accounting; NOT validation of Omega",
        "electron_positron_cm_threshold_mev": round(threshold, 9),
        "two_head_on_photon_energies_mev": [.6, .6],
        "two_head_on_photon_total_cm_energy_mev": cm_energy,
        "cm_energy_above_pair_threshold_mev": round(excess, 9),
        "fission_example_q_mev": 200,
        "fission_mass_defect_u": round(equivalent_mass_defect_u(200.), 9),
        "deuteron_binding_mass_defect_u": round(equivalent_mass_defect_u(DEUTERON_BINDING_MEV), 9),
        "limits": [
            "Fission does not prove a universal origin of mass.",
            "Mass invariance is not a time dilation factor.",
            "No decay rates or stable-state selection are modeled.",
            "All physics used here is imported, not derived from Omega.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), ensure_ascii=False, indent=2))
