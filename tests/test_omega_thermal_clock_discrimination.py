"""Five synthetic checks for Omega E23. Does NOT test fundamental physics."""
from pathlib import Path
from runpy import run_path
import math

M = run_path(str(Path(__file__).resolve().parents[1] /
                 "scripts" / "check_omega_thermal_clock_discrimination.py"))


def test_thermal_kinetics_without_clock_effect():
    result = M["run_suite"]()
    a = result["scenarios"][0]
    mult = a["reaction_multipliers_per_proper_second"]
    assert 1 < mult["reaction_A"] < mult["reaction_B"]
    assert not a["nominal_five_sigma_detection"]


def test_differential_clock_anomaly_detectable():
    a = M["simulate"]("differential")
    assert a["nominal_five_sigma_detection"]
    assert a["synthetic_clock_difference_after_thermal_correction_ppq"] > 0


def test_common_clock_shift_is_not_locally_identifiable():
    a = M["simulate"]("common")
    assert not a["nominal_five_sigma_detection"]
    for x, y, g in ((1.4, -0.8, .2), (-2., 5., -.13)):
        assert math.isclose((x+g)-(y+g), x-y, abs_tol=1e-14)


def test_thermal_calibration_bias_yields_false_positive():
    a = M["simulate"]("miscalibrated")
    assert a["nominal_five_sigma_detection"]
    assert a["true_clock_anomaly_ppq"] == {"A": 0., "B": 0.}


def test_reproducibility_and_no_real_observation_claim():
    assert M["run_suite"]() == M["run_suite"]()
    assert "SYNTHETIC" in M["run_suite"]()["status"]
