from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

IGNORED_LOCAL_DIRECTORIES = {
    ".git",
    ".idea",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".pytest_cache",
    ".venv",
    ".vscode",
    "__pycache__",
    "build",
    "dist",
    "generated",
    "outputs",
    "venv",
}


def _is_ignored_local_artifact(path: Path) -> bool:
    """Return whether *path* is a disposable local-development artifact."""
    relative = path.relative_to(ROOT)
    if any(
        part in IGNORED_LOCAL_DIRECTORIES or part.endswith(".egg-info")
        for part in relative.parts
    ):
        return True
    name = relative.name
    return (
        name == ".env"
        or name.startswith(".env.")
        or name.endswith((".pyc", ".pyo", ".tmp"))
    )


def _rows(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def verify_manifest() -> tuple[int, list[dict[str, str]]]:
    manifest = ROOT / "manifests" / "PUBLISHED_FILES_SHA256.csv"
    rows = _rows("manifests/PUBLISHED_FILES_SHA256.csv")
    failures: list[dict[str, str]] = []
    for row in rows:
        path = ROOT / row["path"]
        if not path.is_file():
            failures.append({"path": row["path"], "error": "missing"})
            continue
        data = path.read_bytes()
        actual_hash = hashlib.sha256(data).hexdigest()
        actual_size = len(data)
        if actual_hash != row["sha256"] or actual_size != int(row["size_bytes"]):
            failures.append(
                {
                    "path": row["path"],
                    "error": "integrity_mismatch",
                    "expected_sha256": row["sha256"],
                    "actual_sha256": actual_hash,
                    "expected_size": row["size_bytes"],
                    "actual_size": str(actual_size),
                }
            )
    known = {row["path"] for row in rows}
    known.add(str(manifest.relative_to(ROOT)))
    actual = {
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*")
        if path.is_file() and not _is_ignored_local_artifact(path)
    }
    for path in sorted(actual - known):
        failures.append({"path": path, "error": "unmanifested"})
    return len(rows), failures


def verify_denominators() -> dict[str, int]:
    counts = {
        "core_claims": len(_rows("epistemic/CLAIMS_CORE.csv")),
        "traceability_rows": len(_rows("traceability/CLAIM_EVIDENCE_MAP.csv")),
        "verdicts": len(_rows("results/VEREDICTOS_NORMALIZADOS.csv")),
        "negative_limits": len(_rows("negative-results/NEGATIVOS_Y_LIMITES.csv")),
        "reproduction_negatives": len(
            _rows("negative-results/REPRODUCTION_NEGATIVES.csv")
        ),
        "open_questions": len(_rows("open-questions/DUDAS_ABIERTAS.csv")),
        "python_occurrences": len(_rows("validations/CODE_COVERAGE.csv")),
        "python_unique_hashes": len(_rows("manifests/CODE_AUDIT.csv")),
        "primary_figures": len(_rows("manifests/FIGURES_PRIMARY.csv")),
    }
    expected = {
        "core_claims": 20,
        "traceability_rows": 20,
        "verdicts": 210,
        "negative_limits": 307,
        "reproduction_negatives": 14,
        "open_questions": 81,
        "python_occurrences": 40,
        "python_unique_hashes": 28,
        "primary_figures": 7,
    }
    if counts != expected:
        raise RuntimeError({"expected": expected, "actual": counts})
    return counts


def verify_repository_checks() -> dict[str, int]:
    from omega_repro.validate_core import run_checks as run_core
    from omega_repro.validate_deliveries_01_17 import (
        run_checks as run_deliveries,
    )

    core = run_core()
    deliveries = run_deliveries()
    failed = [
        check.name
        for check in [*core, *deliveries]
        if not check.passed
    ]
    if failed:
        raise RuntimeError({"failed_repository_checks": failed})
    return {"core_checks": len(core), "delivery_checks": len(deliveries)}


def main() -> int:
    manifest_rows, integrity_failures = verify_manifest()
    result: dict[str, object] = {
        "manifest_rows": manifest_rows,
        "integrity_failures": integrity_failures,
    }
    if integrity_failures:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 1
    result["denominators"] = verify_denominators()
    result["repository_checks"] = verify_repository_checks()
    result["scope"] = (
        "Integrity and archived-model checks only; no external physical validation."
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
