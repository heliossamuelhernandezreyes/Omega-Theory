"""Unit tests for a conditional two-stage event clock, NOT for physical Omega."""
import importlib.util
import math
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'scripts' / 'check_relational_clock_ratio.py'
spec = importlib.util.spec_from_file_location('omega_R2', path)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


def test_expected_renewal_rate():
    assert math.isclose(M.expected_tick_rate(4, 6), 2.4)
    assert math.isclose(M.expected_tick_rate(5, 5), 2.5)


def test_common_mode_unobservable_in_ratio():
    baseline = M.clock_ratio(0)
    for u in (0, 0.5, 1, 3):
        assert math.isclose(M.clock_ratio(u, False), baseline, rel_tol=1e-14)


def test_relative_mode_changes_count_ratio():
    assert M.clock_ratio(1, True) < M.clock_ratio(0)
    result = M.verify(10000)
    assert abs(result['monte_carlo_relative_ratio'] - result['relative_mode_u1_ratio']) < .025


def test_analytic_log_slope():
    eps = 1e-6
    estimated = -(math.log(M.clock_ratio(eps, True)) - math.log(M.clock_ratio(0, True))) / eps
    slope = M.effective_obstruction_derivative('A', 0) - M.effective_obstruction_derivative('B', 0)
    assert math.isclose(slope, .2)
    assert math.isclose(estimated, slope, rel_tol=1e-5)


def test_topology_alone_cannot_fix_tick_rate():
    assert M.expected_tick_rate(1, 1) == .5
    assert M.expected_tick_rate(2, 2) == 1
    # At each stage, the normalized branching P=1 in BOTH models.


def test_input_validation_and_determinism():
    for args in ((0, 1), (-1, 1), (1, float('inf'))):
        try:
            M.expected_tick_rate(*args)
        except ValueError:
            pass
        else:
            raise AssertionError('Rates must be positive and finite')
    assert M.count_A_ticks_during_B_ticks(1, True, 2000) == M.count_A_ticks_during_B_ticks(1, True, 2000)
