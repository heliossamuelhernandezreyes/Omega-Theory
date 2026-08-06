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

ROOT = Path(__file__).resolve().parents[2] / "data" / "deliveries_01_17"


def run_checks() -> list[Check]:
    records = json.loads((ROOT / "checks.json").read_text(encoding="utf-8"))
    return [Check(**record) for record in records]


def main() -> int:
    checks = run_checks()
    print(json.dumps([asdict(c) for c in checks], indent=2, ensure_ascii=False))
    return 0 if checks and all(c.passed for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
