from omega_repro.validate_deliveries_01_17 import run_checks


def test_archived_deliveries_01_17():
    checks = run_checks()
    failed = [c for c in checks if not c.passed]
    assert len(checks) == 16
    assert not failed, failed
