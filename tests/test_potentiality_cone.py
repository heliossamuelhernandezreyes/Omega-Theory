"""Regresiones internas del prototipo exploratorio; no son validación física."""
from pathlib import Path
from runpy import run_path
import math


MODEL = run_path(str(Path(__file__).resolve().parents[1] / "scripts" / "check_potentiality_cone.py"))


def test_cota_grupo_y_brechas():
    r = MODEL["run_checks"]()
    assert r["max_abs_group_speed"] <= r["speed_bound"] + 1e-12
    assert r["sampled_k_points_per_gap"] == 401
    assert r["gaps"] == [0.0, 0.5, 1.0, 2.0]


def test_error_de_dispersion_no_nulo():
    r = MODEL["run_checks"]()
    assert math.isclose(r["small_ka_relative_omega_sq_error"], -0.000833055605153, abs_tol=1e-12)
    assert math.isclose(r["large_ka_relative_omega_sq_error"], -0.080604611736279, abs_tol=1e-12)
    assert r["large_ka_relative_omega_sq_error"] != 0


def test_factor_comun_no_modifica_ramificaciones():
    f = MODEL["branching"]
    weights = [0.2, 0.4, 1.0]
    assert all(math.isclose(x, y, abs_tol=1e-14)
               for x, y in zip(f(weights), f([7.5 * w for w in weights])))
