from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import json
import pandas as pd

@dataclass
class Check:
    name: str
    passed: bool
    value: float | int | str
    threshold: float | int | str
    source: str


def _data_root() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "selected"


def run_checks() -> list[Check]:
    root = _data_root()
    checks: list[Check] = []

    p = root / "delivery_19__test_04_produccion_entropia.csv"
    if p.exists():
        d = pd.read_csv(p)
        eq = d[d["model"] == "detailed_balance"]["mean_entropy_production"].abs().max()
        driven = d[d["model"] == "driven_ring"]["mean_entropy_production"].min()
        checks.append(Check("detailed balance mean entropy production", bool(eq < 1e-12), float(eq), "<1e-12", p.name))
        checks.append(Check("driven mean entropy production", bool(driven > 0), float(driven), ">0", p.name))

    p = root / "delivery_20__test_02_identidades_canonicas.csv"
    if p.exists():
        d = pd.read_csv(p)
        e1 = float(d["identity1_error"].max())
        e2 = float(d["identity2_error"].max())
        checks.append(Check("canonical identity dlogZ", e1 < 1e-7, e1, "<1e-7", p.name))
        checks.append(Check("canonical identity dU", e2 < 1e-7, e2, "<1e-7", p.name))

    p = root / "delivery_21__test_02_aditividad_energia_frecuencia.csv"
    if p.exists():
        d = pd.read_csv(p).set_index("candidate")
        linear = float(d.loc["linear", "mean_additivity_error"])
        alternatives = float(d.drop(index="linear")["mean_additivity_error"].min())
        checks.append(Check("linear energy-frequency additivity", linear < 1e-12, linear, "<1e-12", p.name))
        checks.append(Check("nonlinear candidates separated", alternatives > 1e-6, alternatives, ">1e-6", p.name))

    p = root / "delivery_18__monotonicity_summary.csv"
    if p.exists():
        d = pd.read_csv(p).iloc[0]
        global_decreases = int(d["total_global_hidden_count_decreases"])
        local_trials = int(d["trials_with_local_macro_entropy_decrease"])
        checks.append(Check("global history count monotonicity", global_decreases == 0, global_decreases, "0", p.name))
        checks.append(Check("local macro entropy can decrease", local_trials > 0, local_trials, ">0", p.name))

    return checks


def main() -> int:
    checks = run_checks()
    print(json.dumps([asdict(c) for c in checks], indent=2, ensure_ascii=False))
    return 0 if checks and all(c.passed for c in checks) else 1

if __name__ == "__main__":
    raise SystemExit(main())
