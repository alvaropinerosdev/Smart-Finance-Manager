"""
Smoke test to verify that the testing environment, test runner,
and project imports are configured and functioning correctly.
"""

from exceptions import DomainValidationError, SmartFinanceError


def test_smoke_environment():
    """Verify that pytest is functioning properly."""
    assert True


def test_smoke_domain_exceptions_import():
    """Verify that domain exceptions in src can be imported and instantiated."""
    err = DomainValidationError("Smoke test validation error")
    assert isinstance(err, SmartFinanceError)
    assert str(err) == "Smoke test validation error"
