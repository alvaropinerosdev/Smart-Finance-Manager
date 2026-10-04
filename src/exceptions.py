"""
Base Exceptions for Smart Finance Manager
"""


class SmartFinanceError(Exception):
    """Base exception for all domain and application errors."""
    pass


class DomainValidationError(SmartFinanceError):
    """Raised when an entity or business invariant validation fails."""
    pass
