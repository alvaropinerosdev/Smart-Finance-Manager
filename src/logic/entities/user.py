"""
User Entity Module.

Defines the root user entity for Smart Finance Manager.
"""

from datetime import datetime, timezone
from typing import Optional
from uuid import UUID

from exceptions import DomainValidationError


class User:
    """
    Root domain entity representing registered system users.
    Acts as the logical owner of categories, financial records, goals, and reports.
    """

    def __init__(
        self,
        id: UUID,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        self._validate_id(id)
        self._validate_datetimes(created_at, updated_at)

        self.id: UUID = id
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at

    @staticmethod
    def _validate_id(user_id: UUID) -> None:
        if not isinstance(user_id, UUID):
            raise DomainValidationError("User id must be a valid UUID instance.")

    @staticmethod
    def _validate_datetimes(
        created_at: datetime, updated_at: datetime
    ) -> None:
        if not isinstance(created_at, datetime):
            raise DomainValidationError("created_at must be a valid datetime instance.")
        if not isinstance(updated_at, datetime):
            raise DomainValidationError("updated_at must be a valid datetime instance.")
        if updated_at < created_at:
            raise DomainValidationError("updated_at cannot be prior to created_at.")

    def update_timestamp(self, dt: Optional[datetime] = None) -> None:
        """
        Update the updated_at timestamp to the specified datetime or the current UTC time.
        """
        now = datetime.now(timezone.utc)
        target = dt if dt is not None else now
        if not isinstance(target, datetime):
            raise DomainValidationError("updated_at must be a valid datetime instance.")
        if target < self.created_at:
            raise DomainValidationError("updated_at cannot be prior to created_at.")
        self.updated_at = target

    def __repr__(self) -> str:
        return f"<User id={self.id}>"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
