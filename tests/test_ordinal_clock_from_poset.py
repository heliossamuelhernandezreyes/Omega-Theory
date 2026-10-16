"""Order-only proof checks. No empirical significance."""
import importlib.util
import math
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "scripts" / "check_ordinal_clock_from_poset.py"
spec = importlib.util.spec_from_file_location("omega_r3", p)
M = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = M
spec.loader.exec_module(M)


def test_unconstrained_combinatorics():
    x = M.build_poset()
    assert x.completion_count() == math.comb(12, 6)
    assert math.isclose(x.expected_A_before_marker("uniform_extension"), 18/7)


def test_selective_causal_links_change_relative_counts():
    result = M.run_checks()
    r = {x["constraint"]: x for x in result["rows"]}
    assert r["A2_before_B3"]["linear_extensions"] == 672
    assert r["B3_before_A2"]["linear_extensions"] == 252
    assert math.isclose(r["A2_before_B3"]["A_events_before_B3_uniform_extensions"], 23/7)
    assert math.isclose(r["B3_before_A2"]["A_events_before_B3_uniform_extensions"], 2/3)


def test_identical_poset_multiple_admissible_measures():
    x = M.build_poset()
    a = x.expected_A_before_marker("uniform_extension")
    b = x.expected_A_before_marker("uniform_enabled")
    assert math.isclose(b, 711/256)
    assert not math.isclose(a, b)


def test_no_absolute_clock_units_or_holding_times():
    result = M.run_checks()
    assert "not seconds" in result["interpretation"]
    assert any("physical holding times" in t for t in result["no_go"])


def test_forced_causal_precedence():
    x = M.build_poset("B3_before_A2")
    assert x.expected_A_before_marker("uniform_extension") < 1.0
    assert x.expected_A_before_marker("uniform_enabled") < 1.0


def test_input_validation_and_determinism():
    assert M.run_checks() == M.run_checks()
    for test in [lambda: M.build_poset("oops"), lambda: M.build_poset(n=2),
                 lambda: M.build_poset().expected_A_before_marker("oops")]:
        try:
            test()
        except ValueError:
            pass
        else:
            raise AssertionError("Expected invalid argument to be rejected")
