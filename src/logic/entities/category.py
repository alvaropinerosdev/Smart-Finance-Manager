"""
Category Entity Module.

Defines the Category domain model for classifying financial records in Smart Finance Manager.
"""

from datetime import datetime, timezone
from typing import Optional
from uuid import UUID

from exceptions import DomainValidationError


class Category:
    """
    Domain entity representing transaction categories for financial classification.
    """

    def __init__(
        self,
        id: UUID,
        user_id: UUID,
        name: str,
        type: str,
        is_default: bool,
        created_at: datetime,
        updated_at: Optional[datetime] = None,
        deleted_at: Optional[datetime] = None,
    ) -> None:
        self._validate_ids(id, user_id)
        self._validate_name(name)
        self._validate_type(type)
        self._validate_is_default(is_default)
        self._validate_datetimes(created_at, updated_at, deleted_at)

        self.id: UUID = id
        self.user_id: UUID = user_id
        self.name: str = name.strip()
        self.type: str = type.strip().upper()
        self.is_default: bool = is_default
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at if updated_at is not None else created_at
        self.deleted_at: Optional[datetime] = deleted_at

    @staticmethod
    def _validate_ids(id: UUID, user_id: UUID) -> None:
        if not isinstance(id, UUID):
            raise DomainValidationError("Category id must be a valid UUID instance.")
        if not isinstance(user_id, UUID):
            raise DomainValidationError("user_id must be a valid UUID instance.")

    @staticmethod
    def _validate_name(name: str) -> None:
        if not isinstance(name, str):
            raise DomainValidationError("Category name must be a string.")
        stripped = name.strip()
        if not stripped:
            raise DomainValidationError("Category name cannot be empty or blank.")
        if len(stripped) > 100:
            raise DomainValidationError("Category name cannot exceed 100 characters.")

    @staticmethod
    def _validate_type(category_type: str) -> None:
        if not isinstance(category_type, str):
            raise DomainValidationError("Category type must be a string.")
        normalized = category_type.strip().upper()
        if normalized not in ("INCOME", "EXPENSE"):
            raise DomainValidationError(
                f"Category type '{category_type}' is invalid. Must be 'INCOME' or 'EXPENSE'."
            )

    @staticmethod
    def _validate_is_default(is_default: bool) -> None:
        if not isinstance(is_default, bool):
            raise DomainValidationError("is_default must be a boolean.")

    @staticmethod
    def _validate_datetimes(
        created_at: datetime,
        updated_at: Optional[datetime],
        deleted_at: Optional[datetime],
    ) -> None:
        if not isinstance(created_at, datetime):
            raise DomainValidationError("created_at must be a valid datetime instance.")
        if updated_at is not None:
            if not isinstance(updated_at, datetime):
                raise DomainValidationError("updated_at must be a valid datetime instance.")
            if updated_at < created_at:
                raise DomainValidationError("updated_at cannot be prior to created_at.")
        if deleted_at is not None:
            if not isinstance(deleted_at, datetime):
                raise DomainValidationError("deleted_at must be a valid datetime instance.")
            if deleted_at < created_at:
                raise DomainValidationError("deleted_at cannot be prior to created_at.")

    def rename(self, new_name: str) -> None:
        """
        Rename the category with validation and update updated_at.
        """
        self._validate_name(new_name)
        self.name = new_name.strip()
        self.updated_at = datetime.now(timezone.utc)

    def accepts(self, record_type: str) -> bool:
        """
        Check whether this category accepts the given record type ('INCOME' or 'EXPENSE').
        """
        if not isinstance(record_type, str):
            return False
        return self.type == record_type.strip().upper()

    def soft_delete(self) -> None:
        """
        Mark category as soft deleted and refresh timestamps.
        """
        now = datetime.now(timezone.utc)
        self.deleted_at = now
        self.updated_at = now

    def is_active(self) -> bool:
        """
        Return True if category is currently active (not soft deleted).
        """
        return self.deleted_at is None

    def __repr__(self) -> str:
        return f"<Category id={self.id} name='{self.name}' type='{self.type}' active={self.is_active()}>"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Category):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
