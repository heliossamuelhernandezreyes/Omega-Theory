#!/usr/bin/env python3
"""Omega E23: reproducible *synthetic* experiment, not empirical validation.
Compare independently temperature-sensitive reactions with two clock species.
Do not confuse kinetic rates per proper second with elapsed proper time.
"""
from __future__ import annotations
import argparse
import csv
import json
import math
import random
from pathlib import Path

KB_EV_K = 8.617333262145e-5
T_COLD = 300.0
T_HOT = 340.0
ACTIVATION_EV = {"reaction_A": 0.15, "reaction_B": 0.42}
# Artificial values in parts per 10^15; NOT real atomic-species calibrations.
CLOCK_BETA_PPQ = {"clock_A": -2.0, "clock_B": -4.5}
NOISE_PPQ = 0.20
REPEATS = 64
ANOMALY_PPQ = 0.18


def reaction_multiplier(ea_ev: float, t0: float, t1: float) -> float:
    """k(T1)/k(T0) for a toy Arrhenius process, fixed prefactor."""
    if ea_ev <= 0 or t0 <= 0 or t1 <= 0:
        raise ValueError("Ea and absolute temperatures must be positive")
    return math.exp((ea_ev / KB_EV_K) * (1 / t0 - 1 / t1))


def thermal_increment(t0: float, t1: float) -> float:
    return (t1 / t0) ** 4 - 1


def summary(data: list[float]) -> tuple[float, float]:
    mean = sum(data) / len(data)
    if len(data) < 2:
        return mean, float("nan")
    variance = sum((x - mean)**2 for x in data) / (len(data) - 1)
    return mean, math.sqrt(variance)


def simulate(mode: str, seed: int = 20261016, n: int = REPEATS,
             beta_bias_A: float = 0.0) -> dict:
    """clock readings are fractional *shifts* in parts per 1e15, linearized.
    modes: null, differential, common, miscalibrated (false differential).
    Clock readings reported to external reference; clocks located at same site.
    """
    if mode not in ("null", "differential", "common", "miscalibrated"):
        raise ValueError(mode)
    if n < 3:
        raise ValueError("n must be >= 3")
    rng = random.Random(seed)
    d = thermal_increment(T_COLD, T_HOT)
    anomaly = {
        "null": (0.0, 0.0),
        "differential": (+ANOMALY_PPQ, -ANOMALY_PPQ),
        "common": (+ANOMALY_PPQ, +ANOMALY_PPQ),
        "miscalibrated": (0.0, 0.0),
    }[mode]
    if mode == "miscalibrated":
        beta_bias_A = 0.65  # intentional uncorrected thermal response

    # Both clock species experience the same spacetime geometry; no geometry
    # change is simulated. The environmental shifts are subtracted separately.
    cold = []
    hot = []
    for _ in range(n):
        cold.append((rng.gauss(0, NOISE_PPQ), rng.gauss(0, NOISE_PPQ)))
        hot.append((
            (CLOCK_BETA_PPQ["clock_A"] + beta_bias_A)*d
            + anomaly[0] + rng.gauss(0, NOISE_PPQ),
            CLOCK_BETA_PPQ["clock_B"]*d
            + anomaly[1] + rng.gauss(0, NOISE_PPQ),
        ))
    # Remove each calibrated thermal systematic from the clock readings.
    residual_cold = [a-b for a, b in cold]
    residual_hot = [a-b - (CLOCK_BETA_PPQ["clock_A"]-
                                      CLOCK_BETA_PPQ["clock_B"])*d
                    for a, b in hot]
    before_mean, before_sd = summary(residual_cold)
    after_mean, after_sd = summary(residual_hot)
    effect = after_mean-before_mean
    se = math.sqrt(before_sd**2/n + after_sd**2/n)
    z = effect/se
    # A statistically significant A/B difference is NOT automatically a new
    # fundamental phenomenon; it might be an unmodeled differential systematic.
    return {
        "scenario": mode,
        "seed": seed,
        "n_repeats_each_phase": n,
        "cold_K": T_COLD,
        "hot_K": T_HOT,
        "reaction_multipliers_per_proper_second": {
            k: reaction_multiplier(ea, T_COLD, T_HOT)
            for k, ea in ACTIVATION_EV.items()
        },
        "synthetic_clock_difference_after_thermal_correction_ppq": effect,
        "standard_error_ppq": se,
        "z_score": z,
        "nominal_five_sigma_detection": abs(z) >= 5,
        "true_clock_anomaly_ppq": {
            "A": anomaly[0], "B": anomaly[1]},
        "actual_thermal_beta_bias_A_ppq": beta_bias_A,
        "differential_clock_ratio_identifies_common_factor": False,
    }


def run_suite(seed: int = 20261016, n: int = REPEATS) -> dict:
    cases = [simulate(mode, seed=seed, n=n)
             for mode in ("null", "differential", "common", "miscalibrated")]
    c = {a["scenario"]: a for a in cases}
    assert not c["null"]["nominal_five_sigma_detection"]
    assert c["differential"]["nominal_five_sigma_detection"]
    assert not c["common"]["nominal_five_sigma_detection"]
    assert c["miscalibrated"]["nominal_five_sigma_detection"]
    # Exact degeneracy in co-located clock-ratio measurements:
    # (fA+gamma)-(fB+gamma) = fA-fB.
    for a, b, gamma in [(2.0, 3.0, 0.18), (-5.0, 5.0, -0.7)]:
        assert math.isclose((a+gamma)-(b+gamma), a-b, abs_tol=1e-14)
    return {
        "experiment": "Omega E23 - thermal reactions vs differential clocks",
        "status": "SYNTHETIC PASS, not observations or a GR/quantum theory test",
        "unit_of_clock_shift": "parts per 10^15 fractional frequency",
        "temperature_increment": thermal_increment(T_COLD, T_HOT),
        "assumptions": [
            "Same gravitational background before and after stimulation",
            "Arrhenius factors are illustrative and independent of clock behavior",
            "Two co-located clocks have different invented thermal coefficients",
            "No explicit physics of antimatter or black hole interior",
            "Measurements assume iid Gaussian noise and known calibration",
            "A common clock shift cancels in co-located clock ratios",
            "A thermal calibration error can mimic nonstandard clock physics",
        ],
        "scenarios": cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20261016)
    parser.add_argument("--repeats", type=int, default=REPEATS)
    parser.add_argument("--out", type=Path, default=None,
                        help="optional directory for JSON and CSV reports")
    args = parser.parse_args()
    result = run_suite(seed=args.seed, n=args.repeats)
    if args.out:
        args.out.mkdir(exist_ok=True, parents=True)
        (args.out / "omega_e23_results.json").write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf8")
        fields = ["scenario", "synthetic_clock_difference_after_thermal_correction_ppq",
                  "standard_error_ppq", "z_score", "nominal_five_sigma_detection"]
        with (args.out / "omega_e23_summary.csv").open("w", newline="", encoding="utf8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for scenario in result["scenarios"]:
                writer.writerow({k: scenario[k] for k in fields})
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
