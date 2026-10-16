"""Regresion de un modelo de tasas, no verificacion de fisica de Omega."""
from pathlib import Path
from runpy import run_path
import math


M = run_path(str(Path(__file__).resolve().parents[1] /
                 "scripts" / "check_omega_channels_vs_proper_time.py"))


def test_same_radius_heavier_hole_slows_static_clock():
    result = M["run_checks"]()
    assert math.isclose(result["clock_lapse_before"], 0.707106781, rel_tol=1e-8)
    assert math.isclose(result["clock_lapse_after"], 0.612372436, rel_tol=1e-8)
    assert result["clock_lapse_after"] < result["clock_lapse_before"]


def test_independent_local_rate_can_exceed_lapse_reduction():
    result = M["run_checks"]()
    assert math.isclose(
        result["local_rate_factor_to_increase_received_signal_rate"],
        math.sqrt(4 / 3), rel_tol=1e-8
    )
    rows = result["cases"]
    assert rows[1]["observed_rate_divided_by_initial"] < 1
    assert rows[2]["observed_rate_divided_by_initial"] > 1
    assert rows[3]["total_events_per_proper_s"] == 1.5


def test_no_outgoing_classical_signal_if_escape_zero():
    result = M["run_checks"]()
    assert M["counts_per_asymptotic_second"](
        1.5, result["clock_lapse_after"], escape_fraction=0
    ) == 0


def test_horizon_excluded_from_stationary_clock_formula():
    rs = M["schwarzschild_radius"](25)
    try:
        M["lapse_static_exterior"](25, rs)
    except ValueError:
        pass
    else:
        raise AssertionError("No stationary emitter on event horizon")
