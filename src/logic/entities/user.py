"""
User Entity Module.

Defines the root user entity for Smart Finance Manager.
"""

from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

from exceptions import DomainValidationError


class User:
    """
    Root domain entity representing registered system users.
    Acts as the logical owner of categories, financial records, goals, and reports.
    """

    def __init__(
        self,
        id: Optional[UUID] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        self._validate_id(id)
        self._validate_datetimes(created_at, updated_at)

        now = datetime.now(timezone.utc)
        self.id: UUID = id if id is not None else uuid4()
        self.created_at: datetime = created_at if created_at is not None else now
        self.updated_at: datetime = updated_at if updated_at is not None else now

    @staticmethod
    def _validate_id(user_id: Optional[UUID]) -> None:
        if user_id is not None and not isinstance(user_id, UUID):
            raise DomainValidationError("User id must be a valid UUID instance.")

    @staticmethod
    def _validate_datetimes(
        created_at: Optional[datetime], updated_at: Optional[datetime]
    ) -> None:
        if created_at is not None and not isinstance(created_at, datetime):
            raise DomainValidationError("created_at must be a valid datetime instance.")
        if updated_at is not None and not isinstance(updated_at, datetime):
            raise DomainValidationError("updated_at must be a valid datetime instance.")
        if (
            created_at is not None
            and updated_at is not None
            and updated_at < created_at
        ):
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

