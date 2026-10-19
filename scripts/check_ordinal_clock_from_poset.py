#!/usr/bin/env python3
"""Omega R3: order-only clock comparison and non-identifiability proof.

No metric time, no stochastic rates, no physical derivation of Omega.
All linear extensions are finite and exactly enumerated via dynamic programming.
Two admissible history-selection measures are deliberately contrasted.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
import argparse
import json
import math


@dataclass(frozen=True)
class Poset:
    labels: tuple[str, ...]
    prerequisite_masks: tuple[int, ...]
    marker: str

    @property
    def full(self) -> int:
        return (1 << len(self.labels)) - 1

    def eligible(self, mask: int) -> tuple[int, ...]:
        return tuple(i for i, p in enumerate(self.prerequisite_masks)
                     if not mask & (1 << i) and p & mask == p)

    @lru_cache(maxsize=None)
    def completion_count(self, mask: int = 0) -> int:
        if mask == self.full:
            return 1
        return sum(self.completion_count(mask | (1 << i))
                   for i in self.eligible(mask))

    def expected_A_before_marker(self, measure: str) -> float:
        """Expected A events before B3; no time or rate parameters.

        uniform_extension: all full admissible histories have equal measure.
        uniform_enabled: each locally available next event is equiprobable.
        Neither measure is derived from Omega ontology.
        """
        if measure not in ("uniform_extension", "uniform_enabled"):
            raise ValueError(f"Unsupported measure: {measure}")
        marker = self.labels.index(self.marker)

        @lru_cache(maxsize=None)
        def recurse(mask: int) -> float:
            if mask & (1 << marker):
                return 0.0
            available = self.eligible(mask)
            if not available:
                raise AssertionError("Marker unreachable: check poset")
            n = self.completion_count(mask)
            total = 0.0
            for i in available:
                next_mask = mask | (1 << i)
                p = (self.completion_count(next_mask) / n
                     if measure == "uniform_extension"
                     else 1.0 / len(available))
                if i != marker:
                    total += p * ((1.0 if self.labels[i].startswith("A") else 0.0)
                                  + recurse(next_mask))
            return total
        return recurse(0)


def build_poset(cross_constraint: str = "none", n: int = 6) -> Poset:
    if n < 3 or n > 9:
        raise ValueError("3 <= n <= 9 for exact enumeration")
    labels = tuple(f"A{i + 1}" for i in range(n)) + tuple(
        f"B{i + 1}" for i in range(n))
    prerequisites = [0] * (2 * n)
    for i in range(1, n):
        prerequisites[i] |= 1 << (i - 1)
        prerequisites[n + i] |= 1 << (n + i - 1)
    if cross_constraint == "A2_before_B3":
        prerequisites[n + 2] |= 1 << 1
    elif cross_constraint == "B3_before_A2":
        prerequisites[1] |= 1 << (n + 2)
    elif cross_constraint != "none":
        raise ValueError("Unsupported causal constraint")
    poset = Poset(labels, tuple(prerequisites), marker="B3")
    if poset.completion_count() <= 0:
        raise AssertionError("Cyclic causal constraints")
    return poset


def run_checks() -> dict:
    rows = []
    for name in ("none", "A2_before_B3", "B3_before_A2"):
        model = build_poset(name)
        rows.append({
            "constraint": name,
            "linear_extensions": model.completion_count(),
            "A_events_before_B3_uniform_extensions":
                model.expected_A_before_marker("uniform_extension"),
            "A_events_before_B3_uniform_enabled":
                model.expected_A_before_marker("uniform_enabled"),
        })
    r = {x["constraint"]: x for x in rows}
    assert r["none"]["linear_extensions"] == math.comb(12, 6) == 924
    assert r["A2_before_B3"]["linear_extensions"] == 672
    assert r["B3_before_A2"]["linear_extensions"] == 252
    assert math.isclose(r["none"]["A_events_before_B3_uniform_extensions"], 18 / 7)
    assert math.isclose(r["A2_before_B3"]["A_events_before_B3_uniform_extensions"], 23 / 7)
    assert math.isclose(r["B3_before_A2"]["A_events_before_B3_uniform_extensions"], 2 / 3)
    assert math.isclose(r["none"]["A_events_before_B3_uniform_enabled"], 711 / 256)
    assert not math.isclose(r["none"]["A_events_before_B3_uniform_extensions"],
                            r["none"]["A_events_before_B3_uniform_enabled"])
    assert r["B3_before_A2"]["A_events_before_B3_uniform_extensions"] < \
        r["none"]["A_events_before_B3_uniform_extensions"] < \
        r["A2_before_B3"]["A_events_before_B3_uniform_extensions"]
    return {
        "status": "PASS: exact ordinal toy combinatorics; NO physics validation",
        "n_events_per_clock": 6,
        "reference_event": "B3",
        "interpretation": "Expected count of A events prior to B3; not seconds",
        "rows": rows,
        "no_go": [
            "Same poset admits different order-respecting probability measures",
            "Causal ordering fixes neither measure nor physical holding times",
            "Uniform full histories and uniform eligible events are extra inequivalent assumptions",
            "Even a total order has no absolute duration without an operational scale",
            "No derivation of black-hole clock, antimatter, GR, or Omega q_e",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = run_checks()
    print(json.dumps(result, ensure_ascii=False, indent=2))
