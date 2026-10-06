"""
FinancialRecord Entity Module.

Defines the abstract base class for all monetary movements in Smart Finance Manager.
"""

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional
from uuid import UUID, uuid4

from exceptions import DomainValidationError


class FinancialRecord(ABC):
    """
    Abstract base class representing a generic financial transaction.
    Encapsulates transactional fields, identifiers, audit timestamps, and core validation.
    """

    type: str

    def __init__(
        self,
        user_id: UUID,
        category_id: UUID,
        amount: Decimal,
        currency: str,
        transaction_datetime: datetime,
        description: Optional[str] = None,
        payment_method: Optional[str] = None,
        location: Optional[str] = None,
        id: Optional[UUID] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        deleted_at: Optional[datetime] = None,
        type: Optional[str] = None,
    ) -> None:
        self._validate_amount(amount)
        self._validate_currency(currency)
        self._validate_ids(user_id, category_id, id)
        self._validate_datetime(transaction_datetime)

        now = datetime.now(timezone.utc)
        self.id: UUID = id if id is not None else uuid4()
        self.user_id: UUID = user_id
        self.category_id: UUID = category_id

        if type is not None:
            self._validate_type(type)
            self.type = type.strip().upper()
        elif hasattr(self, "type") and self.type is not None:
            self._validate_type(self.type)
        else:
            raise DomainValidationError("Record type must be defined.")

        self.amount: Decimal = amount
        self.currency: str = currency.strip().upper()
        self.transaction_datetime: datetime = transaction_datetime
        self.description: Optional[str] = description
        self.payment_method: Optional[str] = payment_method
        self.location: Optional[str] = location
        self.created_at: datetime = created_at if created_at is not None else now
        self.updated_at: datetime = updated_at if updated_at is not None else now
        self.deleted_at: Optional[datetime] = deleted_at

    @staticmethod
    def _validate_type(record_type: str) -> None:
        if not isinstance(record_type, str):
            raise DomainValidationError("Type must be a string.")
        normalized = record_type.strip().upper()
        if normalized not in ("INCOME", "EXPENSE"):
            raise DomainValidationError(
                f"Record type '{record_type}' is invalid. Must be 'INCOME' or 'EXPENSE'."
            )

    @staticmethod
    def _validate_amount(amount: Decimal) -> None:
        if not isinstance(amount, Decimal):
            raise DomainValidationError("Amount must be an instance of Decimal.")
        if amount <= Decimal("0"):
            raise DomainValidationError("Amount must be strictly positive (greater than 0).")

    @staticmethod
    def _validate_currency(currency: str) -> None:
        if not isinstance(currency, str):
            raise DomainValidationError("Currency must be a string.")
        normalized = currency.strip().upper()
        if len(normalized) != 3 or not normalized.isalpha():
            raise DomainValidationError(
                f"Currency '{currency}' is invalid. Must be an ISO 4217 3-letter uppercase code (e.g., 'USD')."
            )

    @staticmethod
    def _validate_ids(user_id: UUID, category_id: UUID, id: Optional[UUID]) -> None:
        if not isinstance(user_id, UUID):
            raise DomainValidationError("user_id must be a valid UUID instance.")
        if not isinstance(category_id, UUID):
            raise DomainValidationError("category_id must be a valid UUID instance.")
        if id is not None and not isinstance(id, UUID):
            raise DomainValidationError("id must be a valid UUID instance.")

    @staticmethod
    def _validate_datetime(dt: datetime) -> None:
        if not isinstance(dt, datetime):
            raise DomainValidationError("transaction_datetime must be a valid datetime instance.")

    @abstractmethod
    def signed_amount(self) -> Decimal:
        """
        Return the signed monetary impact of the transaction.
        Must be implemented by concrete subclasses (positive for Income, negative for Expense).
        """
        pass