from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import json

@dataclass
class Check:
    name: str
    delivery: int
    passed: bool
    value: float | int | str
    criterion: str

ROOT = Path(__file__).resolve().parents[2] / "data" / "derived" / "deliveries_01_17"


def _evaluate(value: float | int, criterion: str) -> bool:
    if criterion.startswith("<") and not criterion.startswith("<="):
        return float(value) < float(criterion[1:])
    if criterion.startswith("<="):
        return float(value) <= float(criterion[2:])
    if criterion.startswith(">"):
        return float(value) > float(criterion.split()[0][1:])
    if criterion.startswith("="):
        return float(value) == float(criterion[1:])
    if "/" in criterion:
        numerator, denominator = criterion.split("/", 1)
        return int(value) == int(numerator) == int(denominator)
    raise ValueError(f"Unsupported criterion: {criterion}")


def run_checks() -> list[Check]:
    records = json.loads((ROOT / "checks.json").read_text(encoding="utf-8"))
    checks: list[Check] = []
    for record in records:
        passed = _evaluate(record["value"], record["criterion"])
        checks.append(Check(
            name=record["name"],
            delivery=int(record["delivery"]),
            passed=passed,
            value=record["value"],
            criterion=record["criterion"],
        ))
    return checks


def main() -> int:
    checks = run_checks()
    print(json.dumps([asdict(c) for c in checks], indent=2, ensure_ascii=False))
    return 0 if checks and all(c.passed for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
