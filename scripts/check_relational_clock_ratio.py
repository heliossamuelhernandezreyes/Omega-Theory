#!/usr/bin/env python3
"""Omega R2: conditional operational clock ratios from event-network weights.

Not a derivation of proper time, atomic transition frequencies, or gravity.
A 'clock' is a two-stage renewal chain unrolled across ontological events:
A_n -> B_n -> A_(n+1), never a return to an identical ontological state.
"""
from __future__ import annotations
import argparse
import json
import math
import random

CLOCKS = {"A": (4.0, 6.0), "B": (5.0, 5.0)}
COMMON_Q = 0.40
RELATIVE_Q = {"A": (0.0, 0.50), "B": (0.0, 0.0)}


def rates(clock: str, u: float, relative: bool) -> tuple[float, float]:
    """Omega-inspired r_e(u) = r_e(0) exp[-(s0+delta_e)u]."""
    if clock not in CLOCKS or not math.isfinite(u) or u < 0:
        raise ValueError('unknown clock or invalid nonnegative obstruction u')
    r0 = CLOCKS[clock]
    delta = RELATIVE_Q[clock] if relative else (0.0, 0.0)
    return tuple(r * math.exp(-(COMMON_Q + d) * u)
                 for r, d in zip(r0, delta))


def expected_tick_rate(a: float, b: float) -> float:
    """Renewal theorem: one completed tick per mean wait (1/a + 1/b)."""
    if not (math.isfinite(a) and math.isfinite(b) and a > 0 and b > 0):
        raise ValueError('positive finite rates required')
    return a * b / (a + b)


def clock_ratio(u: float, relative: bool = False) -> float:
    return expected_tick_rate(*rates('A', u, relative)) / expected_tick_rate(
        *rates('B', u, relative))


def effective_obstruction_derivative(clock: str, u: float) -> float:
    """- d ln(tick_rate)/du = (b*q_a + a*q_b)/(a+b), exact."""
    a, b = rates(clock, u, relative=True)
    da, db = RELATIVE_Q[clock]
    qa, qb = COMMON_Q + da, COMMON_Q + db
    return (b * qa + a * qb) / (a + b)


def count_A_ticks_during_B_ticks(u: float, relative: bool, n_B: int,
                                 seed: int = 20261016) -> float:
    """Simulate ONLY the dimensionless tick-count ratio N_A/N_B.

    A and B are two independent two-stage exponential renewal processes.
    An auxiliary simulation parameter determines event ordering; its absolute
    scale is not an output and cancels under simultaneous rate scaling.
    """
    if n_B < 100:
        raise ValueError('n_B must be >= 100')
    ra, rb = rates('A', u, relative), rates('B', u, relative)
    random_B = random.Random(seed)
    random_A = random.Random(seed + 1)
    end_parameter = (random_B.gammavariate(n_B, 1 / rb[0]) +
                     random_B.gammavariate(n_B, 1 / rb[1]))
    elapsed = 0.0
    count = 0
    while True:
        elapsed += (random_A.expovariate(ra[0]) +
                    random_A.expovariate(ra[1]))
        if elapsed > end_parameter:
            break
        count += 1
    return count / n_B


def verify(n_B: int = 30000) -> dict:
    at_zero = clock_ratio(0.0)
    common = clock_ratio(1.0, relative=False)
    relative = clock_ratio(1.0, relative=True)
    assert math.isclose(at_zero, 0.96, rel_tol=1e-14)
    assert math.isclose(common, at_zero, rel_tol=1e-14)
    assert relative < at_zero
    eps = 1e-6
    numerical = -(math.log(clock_ratio(eps, True)) -
                  math.log(clock_ratio(0.0, True))) / eps
    expected = (effective_obstruction_derivative('A', 0.0) -
                effective_obstruction_derivative('B', 0.0))
    assert math.isclose(numerical, expected, rel_tol=1e-5, abs_tol=1e-6)
    assert math.isclose(expected, 0.2, abs_tol=1e-14)
    sim_common = count_A_ticks_during_B_ticks(1.0, False, n_B)
    sim_relative = count_A_ticks_during_B_ticks(1.0, True, n_B)
    assert abs(sim_common - common) < 0.025
    assert abs(sim_relative - relative) < 0.025
    # Same unrolled graph and P=1 on each deterministic edge, different rates.
    # Topology/normalized local branching alone cannot fix clock ratios.
    assert expected_tick_rate(1, 1) != expected_tick_rate(2, 2)
    return {
        'status': 'PASS: conditional event-network identity; NOT an empirical validation',
        'baseline_ratio_A_over_B': at_zero,
        'common_mode_u1_ratio': common,
        'relative_mode_u1_ratio': relative,
        'relative_shift_percent': 100 * (relative / at_zero - 1),
        'minus_log_ratio_derivative_at_u0': expected,
        'monte_carlo_B_ticks': n_B,
        'monte_carlo_common_ratio': sim_common,
        'monte_carlo_relative_ratio': sim_relative,
        'clock_rates_u1_common': {c: rates(c, 1, False) for c in CLOCKS},
        'clock_rates_u1_relative': {c: rates(c, 1, True) for c in CLOCKS},
        'limitations': [
            'Exponential waiting times and auxiliary parameter are extra axioms',
            'Clock weights and obstructions are illustrative, not derived from Gamma alone',
            'Clock ticks are stochastic transitions, not optical atomic frequencies',
            'Common rescaling of all rates leaves relative observations unchanged',
            'No proper time, black hole, antimatter microphysics or metric derived',
        ],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--B-ticks', type=int, default=30000)
    args = parser.parse_args()
    print(json.dumps(verify(n_B=args.B_ticks), indent=2, ensure_ascii=False))
