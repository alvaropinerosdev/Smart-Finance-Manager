"""
Unit tests for User and Category entities.
"""

from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid4

import pytest

from exceptions import DomainValidationError
from logic.entities import User


@pytest.fixture
def sample_user_id() -> UUID:
    return uuid4()


@pytest.fixture
def sample_created_at() -> datetime:
    return datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)


@pytest.fixture
def sample_updated_at(sample_created_at: datetime) -> datetime:
    return sample_created_at + timedelta(days=1)


class TestUserEntity:
    """Tests verifying User entity lifecycle and behavior."""

    def test_cannot_instantiate_user_without_required_arguments(self):
        with pytest.raises(TypeError):
            User()  # type: ignore

    def test_cannot_instantiate_user_with_missing_arguments(
        self, sample_user_id: UUID, sample_created_at: datetime
    ):
        with pytest.raises(TypeError):
            User(id=sample_user_id)  # type: ignore

        with pytest.raises(TypeError):
            User(id=sample_user_id, created_at=sample_created_at)  # type: ignore

    def test_create_user_success(
        self,
        sample_user_id: UUID,
        sample_created_at: datetime,
        sample_updated_at: datetime,
    ):
        user = User(
            id=sample_user_id,
            created_at=sample_created_at,
            updated_at=sample_updated_at,
        )
        assert user.id == sample_user_id
        assert user.created_at == sample_created_at
        assert user.updated_at == sample_updated_at

    def test_user_equality_and_hash(
        self, sample_created_at: datetime, sample_updated_at: datetime
    ):
        common_id = uuid4()
        user1 = User(
            id=common_id,
            created_at=sample_created_at,
            updated_at=sample_updated_at,
        )
        user2 = User(
            id=common_id,
            created_at=sample_created_at,
            updated_at=sample_updated_at,
        )
        user3 = User(
            id=uuid4(),
            created_at=sample_created_at,
            updated_at=sample_updated_at,
        )

        assert user1 == user2
        assert user1 != user3
        assert user1 != "not-a-user"
        assert hash(user1) == hash(user2)
        assert {user1, user2} == {user1}

    def test_user_repr(
        self,
        sample_user_id: UUID,
        sample_created_at: datetime,
        sample_updated_at: datetime,
    ):
        user = User(
            id=sample_user_id,
            created_at=sample_created_at,
            updated_at=sample_updated_at,
        )
        assert repr(user) == f"<User id={sample_user_id}>"

    def test_update_timestamp_default(
        self, sample_user_id: UUID, sample_created_at: datetime
    ):
        user = User(
            id=sample_user_id,
            created_at=sample_created_at,
            updated_at=sample_created_at,
        )
        initial_updated_at = user.updated_at

        user.update_timestamp()
        assert user.updated_at >= initial_updated_at

    def test_update_timestamp_explicit(
        self, sample_user_id: UUID, sample_created_at: datetime
    ):
        user = User(
            id=sample_user_id,
            created_at=sample_created_at,
            updated_at=sample_created_at,
        )
        new_timestamp = sample_created_at + timedelta(days=5)

        user.update_timestamp(new_timestamp)
        assert user.updated_at == new_timestamp


class TestUserValidation:
    """Tests validating User domain invariants and error handling."""

    def test_reject_invalid_user_id(
        self, sample_created_at: datetime, sample_updated_at: datetime
    ):
        with pytest.raises(DomainValidationError, match="User id must be a valid UUID"):
            User(
                id="invalid-uuid",  # type: ignore
                created_at=sample_created_at,
                updated_at=sample_updated_at,
            )

        with pytest.raises(DomainValidationError, match="User id must be a valid UUID"):
            User(
                id=12345,  # type: ignore
                created_at=sample_created_at,
                updated_at=sample_updated_at,
            )

    def test_reject_invalid_created_at(
        self, sample_user_id: UUID, sample_updated_at: datetime
    ):
        with pytest.raises(DomainValidationError, match="created_at must be a valid datetime"):
            User(
                id=sample_user_id,
                created_at="2026-01-01",  # type: ignore
                updated_at=sample_updated_at,
            )

    def test_reject_invalid_updated_at(
        self, sample_user_id: UUID, sample_created_at: datetime
    ):
        with pytest.raises(DomainValidationError, match="updated_at must be a valid datetime"):
            User(
                id=sample_user_id,
                created_at=sample_created_at,
                updated_at=123456789,  # type: ignore
            )

    def test_reject_updated_at_prior_to_created_at(self, sample_user_id: UUID):
        created = datetime(2026, 2, 1, 10, 0, tzinfo=timezone.utc)
        updated = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)

        with pytest.raises(DomainValidationError, match="updated_at cannot be prior to created_at"):
            User(id=sample_user_id, created_at=created, updated_at=updated)

    def test_reject_update_timestamp_invalid_type(
        self, sample_user_id: UUID, sample_created_at: datetime
    ):
        user = User(
            id=sample_user_id,
            created_at=sample_created_at,
            updated_at=sample_created_at,
        )
        with pytest.raises(DomainValidationError, match="updated_at must be a valid datetime"):
            user.update_timestamp("invalid-date")  # type: ignore

    def test_reject_update_timestamp_prior_to_created_at(
        self, sample_user_id: UUID, sample_created_at: datetime
    ):
        user = User(
            id=sample_user_id,
            created_at=sample_created_at,
            updated_at=sample_created_at,
        )
        prior_date = sample_created_at - timedelta(days=1)

        with pytest.raises(DomainValidationError, match="updated_at cannot be prior to created_at"):
            user.update_timestamp(prior_date)


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__] + sys.argv[1:]))
