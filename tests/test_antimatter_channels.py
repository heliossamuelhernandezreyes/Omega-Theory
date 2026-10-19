"""Regression only: imported relativistic pair thresholds and conserved charges."""
from pathlib import Path
from runpy import run_path
import math

M = run_path(str(Path(__file__).resolve().parents[1] /
                 "scripts" / "check_antimatter_channels.py"))


def test_collider_geometry_changes_possible_continuations():
    results = M["run_checks"]()
    assert results["status"].startswith("PASS")
    cases = results["two_photon_example"]
    assert [c["pair_creation_kinematically_allowed"] for c in cases] == [
        False, False, True
    ]
    assert math.isclose(cases[2]["invariant_energy_mev"], 1.2)
    assert math.isclose(cases[0]["invariant_energy_mev"], 0)


def test_additive_quantum_number_accounting():
    t = M["totals"]
    assert t(("electron", "positron")) == t(("photon", "photon"))
    assert t(("proton",)) == t(("neutron", "positron", "nu_e"))
    assert t(("proton", "antiproton")) == (0, 0, 0)
