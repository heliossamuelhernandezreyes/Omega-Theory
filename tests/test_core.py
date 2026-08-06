from omega_repro.validate_core import run_checks


def test_curated_numeric_checks():
    checks = run_checks()
    assert checks
    assert all(check.passed for check in checks), [check for check in checks if not check.passed]
