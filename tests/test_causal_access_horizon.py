"""Regresión de la hipótesis acceso causal vs actividad local.

Prueba un modelo ilustrativo de alcance causal, no valida un agujero negro
ni genera una derivación de relatividad general a partir de Omega.
"""
from pathlib import Path
from runpy import run_path
import math


MODEL = run_path(str(Path(__file__).resolve().parents[1] /
                     "scripts" / "check_causal_access_horizon.py"))


def test_gravitational_redshift_of_static_outward_radial_beam():
    result = MODEL["run_checks"]()
    assert result["status"].startswith("PASS")
    assert math.isclose(result["schwarzschild_radius_sun_km"],
                        2.953339, abs_tol=1e-6)
    rows = result["static_radial_emitter_cases"]
    assert len(rows) == 5
    for row in rows:
        assert math.isclose(
            row["frequency_at_infinity_over_local"] ** 2,
            row["radial_beam_power_at_infinity_over_local"],
            rel_tol=1e-7, abs_tol=1e-9)


def test_internal_updates_are_possible_without_external_escape():
    result = MODEL["run_checks"]()
    assert result["graph_closed"]["internal_successors_exist"]
    assert not result["graph_closed"]["path_to_infinity_exists"]


def test_no_static_emitter_exactly_at_the_horizon():
    rs = MODEL["schwarzschild_radius"](MODEL["SUN_MASS"])
    try:
        MODEL["redshift_outward"](rs, MODEL["SUN_MASS"])
    except ValueError:
        return
    raise AssertionError("La aproximación de emisor estático no aplica en R=rs")
