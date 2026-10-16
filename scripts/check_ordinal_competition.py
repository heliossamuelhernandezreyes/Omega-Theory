#!/usr/bin/env python3
"""Omega R3: ordinal event competition, without a dimensional clock.

A global update index is an ordering device, NOT physical proper time.
The uniform choice of distinguishable microchannels is an EXTRA postulate.
"""
from __future__ import annotations
import argparse
import json
import math
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class Clock:
    name: str
    channels: tuple[str, ...]
    # Each event advances a phase. Every TWO events completes one tick.
    stages_per_tick: int = 2

    def __post_init__(self) -> None:
        if not self.channels or self.stages_per_tick < 1:
            raise ValueError("Positive number of channels and stages required")


def cardinality(clock: Clock, *, quotient_aliases: bool = False) -> int:
    """Count physical microchannels, or explicitly identified equivalence classes."""
    return len(set(clock.channels)) if quotient_aliases else len(clock.channels)


def exact_ratio(a: Clock, b: Clock, *, quotient_aliases: bool = False) -> float:
    """Expected completed ticks A/B in the long ordinal update sequence."""
    wa = cardinality(a, quotient_aliases=quotient_aliases)
    wb = cardinality(b, quotient_aliases=quotient_aliases)
    return (wa / a.stages_per_tick) / (wb / b.stages_per_tick)


def weighted_ratio(weights_a: tuple[float, ...], weights_b: tuple[float, ...],
                   stages_a: int = 2, stages_b: int = 2) -> float:
    """Same permitted channels, alternative positive microscopic weights.

    Uniform weights are NOT a consequence of the bare graph.
    """
    if (not weights_a or not weights_b or stages_a < 1 or stages_b < 1 or
            any(not math.isfinite(w) or w <= 0 for w in weights_a + weights_b)):
        raise ValueError("All weights must be positive and finite")
    return (sum(weights_a) / stages_a) / (sum(weights_b) / stages_b)


def simulate(clocks: tuple[Clock, ...], n_updates: int = 120000,
             seed: int = 20261016, *, quotient_aliases: bool = False) -> dict:
    """At each ordinal index, uniformly choose among enabled microchannels.

    No dimensional waiting time is sampled. Counts produce dimensionless ratios.
    Distinguishable channels are assumed equally weighted: NOT derived.
    """
    if n_updates < 1 or len(clocks) < 2:
        raise ValueError("Require at least two clocks and a positive update count")
    if len({c.name for c in clocks}) != len(clocks):
        raise ValueError("Clock names must be unique")
    weights = [cardinality(c, quotient_aliases=quotient_aliases) for c in clocks]
    total = sum(weights)
    rng = random.Random(seed)
    updates = [0] * len(clocks)
    for _ in range(n_updates):
        draw = rng.randrange(total)
        for idx, w in enumerate(weights):
            if draw < w:
                updates[idx] += 1
                break
            draw -= w
    ticks = [updates[i] // c.stages_per_tick for i, c in enumerate(clocks)]
    ratios = {f"{clocks[i].name}/{clocks[1].name}": ticks[i] / ticks[1]
              for i in range(len(clocks)) if i != 1}
    return {"counts_updates": dict(zip((c.name for c in clocks), updates)),
            "counts_completed_ticks": dict(zip((c.name for c in clocks), ticks)),
            "completed_tick_ratios_to_second_clock": ratios,
            "ordinal_updates": n_updates,
            "weights": dict(zip((c.name for c in clocks), weights))}


def make_clock(name: str, count: int, *, alias_to_one: bool = False) -> Clock:
    if count < 1:
        raise ValueError("Channel count must be positive")
    channels = (("same_physical_transition",) * count if alias_to_one else
                tuple(f"{name}_channel_{i}" for i in range(count)))
    return Clock(name, channels)


def exact_ordinal_orderings() -> dict:
    """Same two-event poset permits different stochastic measures."""
    orderings = ("A_before_B", "B_before_A")
    return {"allowed_linear_extensions": list(orderings),
            "model_1": {orderings[0]: 0.1, orderings[1]: 0.9},
            "model_2": {orderings[0]: 0.9, orderings[1]: 0.1},
            "same_order_structure": True,
            "measure_not_fixed_by_poset": True}


def run_checks(n_updates: int = 120000) -> dict:
    A1, B1 = make_clock("A", 1), make_clock("B", 1)
    A3, B2 = make_clock("A", 3), make_clock("B", 2)
    experiments = {
        "symmetric": (A1, B1),
        "more_A_microchannels": (A3, B2),
        "restricted_A": (make_clock("A", 1), B2),
        "duplicated_label": (make_clock("A", 2, alias_to_one=True), B1),
    }
    cases = {}
    for label, (a, b) in experiments.items():
        measured = simulate((a, b), n_updates)
        predicted = exact_ratio(a, b)
        ratio = measured["completed_tick_ratios_to_second_clock"]["A/B"]
        # Sampling-error tolerance, generous to avoid probabilistic flaky tests.
        assert abs(ratio - predicted) < .05
        cases[label] = {"exact_A_over_B": predicted,
                        "sample_A_over_B": round(ratio, 8),
                        "counts": measured["counts_completed_ticks"]}
    assert cases["symmetric"]["exact_A_over_B"] == 1
    assert cases["more_A_microchannels"]["exact_A_over_B"] == 1.5
    assert cases["restricted_A"]["exact_A_over_B"] == .5
    assert cases["duplicated_label"]["exact_A_over_B"] == 2
    # Declaring those labels as one physical microchannel restores equality.
    quotient = exact_ratio(experiments["duplicated_label"][0], B1,
                           quotient_aliases=True)
    assert quotient == 1
    # A spectator changes counts per *global update*, but not A/B ratio.
    spectator = make_clock("S", 10)
    with_spectator = simulate((A3, B2, spectator), n_updates)
    observed_with_spectator = with_spectator[
        "completed_tick_ratios_to_second_clock"]["A/B"]
    assert abs(observed_with_spectator - 1.5) < .07
    # Common multiplicity rescaling cancels in the A/B ratio.
    assert exact_ratio(make_clock("A", 6), make_clock("B", 4)) == 1.5
    # The same five allowed channels can have different weights and clock ratios.
    weights_uniform = weighted_ratio((1, 1, 1), (1, 1))
    weights_alternative = weighted_ratio((1, 1, 1), (4, 4))
    assert weights_uniform == 1.5 and weights_alternative == 0.375
    # A symmetric POSET does not uniquely select a stochastic measure.
    poset = exact_ordinal_orderings()
    assert poset["model_1"] != poset["model_2"]
    return {
        "status": "PASS: ordinal toy identities; NOT prediction or validation of Omega",
        "uniform_microchannel_postulate": True,
        "no_dimensional_time_used": True,
        "physical_time_derived": False,
        "experiments": cases,
        "duplicate_after_explicit_quotient_exact_A_over_B": quotient,
        "spectator_A_over_B": round(observed_with_spectator, 8),
        "spectator_fraction_updates_A": round(
            with_spectator["counts_updates"]["A"] / n_updates, 8),
        "same_channel_structure_distinct_weights": {
            "uniform_A_over_B": weights_uniform,
            "alternative_A_over_B": weights_alternative},
        "independent_poset_measures": poset,
        "limitations": [
            "Equal prior microchannel weights are an additional postulate",
            "Microchannel equivalence and physical distinguishability are not determined",
            "Changing channel bookkeeping can fake a clock shift",
            "Global ordinal update indices are not a physical reference clock",
            "No Lorentz invariance, metric, mass or gravitational dynamics derived",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--updates', type=int, default=120000)
    args = parser.parse_args()
    print(json.dumps(run_checks(args.updates), ensure_ascii=False, indent=2))
