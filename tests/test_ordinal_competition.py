"""Tests of the explicit equal-microchannel-weight hypothesis (not nature)."""
import importlib.util
from pathlib import Path
import math

SOURCE = Path(__file__).resolve().parents[1] / 'scripts' / 'check_ordinal_competition.py'
spec = importlib.util.spec_from_file_location('omega_R3', SOURCE)
M = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = M
spec.loader.exec_module(M)


def test_symmetry_equal_channels():
    a, b = M.make_clock('A', 1), M.make_clock('B', 1)
    assert M.exact_ratio(a, b) == 1
    assert abs(M.simulate((a, b), 60000)['completed_tick_ratios_to_second_clock']['A/B']-1) < .06


def test_ordinal_competition_ratios_without_seconds():
    assert M.exact_ratio(M.make_clock('A', 3), M.make_clock('B', 2)) == 1.5
    assert M.exact_ratio(M.make_clock('A', 1), M.make_clock('B', 2)) == .5


def test_common_refinement_of_actual_channels_cancels():
    assert M.exact_ratio(M.make_clock('A', 3), M.make_clock('B', 2)) == M.exact_ratio(M.make_clock('A', 6), M.make_clock('B', 4))


def test_duplicate_label_false_signal_and_explicit_quotient():
    a, b = M.make_clock('A', 2, alias_to_one=True), M.make_clock('B', 1)
    assert M.exact_ratio(a, b) == 2
    assert M.exact_ratio(a, b, quotient_aliases=True) == 1


def test_spectator_does_not_change_asymptotic_clock_ratio():
    a, b, s = M.make_clock('A', 3), M.make_clock('B', 2), M.make_clock('S', 10)
    result = M.simulate((a, b, s), 60000)
    assert abs(result['completed_tick_ratios_to_second_clock']['A/B']-1.5) < .09
    assert result['counts_updates']['A'] / 60000 < 0.25


def test_order_only_cannot_determine_probabilities():
    models = M.exact_ordinal_orderings()
    assert models['same_order_structure']
    assert models['model_1'] != models['model_2']
    assert math.isclose(sum(models['model_1'].values()), 1)
    assert math.isclose(sum(models['model_2'].values()), 1)


def test_reproducibility():
    a, b = M.make_clock('A', 3), M.make_clock('B', 2)
    assert M.simulate((a, b), 5000) == M.simulate((a, b), 5000)
    assert M.run_checks(120000)['status'].startswith('PASS')


def test_same_graph_different_weights_different_predictions():
    assert M.weighted_ratio((1, 1, 1), (1, 1)) == 1.5
    assert M.weighted_ratio((1, 1, 1), (4, 4)) == .375
    assert M.exact_ratio(M.make_clock('A', 3), M.make_clock('B', 2)) == 1.5
