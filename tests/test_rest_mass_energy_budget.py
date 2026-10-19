"""Tests for illustrative mass-energy budgets, not a test of Omega ontology."""
from pathlib import Path
from runpy import run_path
import math


M = run_path(str(Path(__file__).resolve().parents[1] /
                 "scripts" / "check_rest_mass_energy_budget.py"))


def test_pair_threshold_and_four_momentum():
    result = M["run_checks"]()
    assert result["status"].startswith("PASS")
    assert math.isclose(result["electron_positron_cm_threshold_mev"],
                        1.021997901, abs_tol=1e-9)
    assert result["cm_energy_above_pair_threshold_mev"] > 0
    # A single null-momentum photon cannot have invariant mass.
    assert M["two_head_on_photons_invariant_energy_mev"](1., 0.) == 0


def test_binding_releases_energy_reducing_rest_mass():
    result = M["run_checks"]()
    assert result["fission_mass_defect_u"] > 0
    assert result["deuteron_binding_mass_defect_u"] > 0
    assert result["fission_mass_defect_u"] > result["deuteron_binding_mass_defect_u"]
