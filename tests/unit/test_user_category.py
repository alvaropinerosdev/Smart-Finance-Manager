"""
Unit tests for User and Category entities.
"""

from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid4

import pytest

from exceptions import DomainValidationError
from logic.entities import User


class TestUserEntity:
    """Tests verifying User entity lifecycle and behavior."""

    def test_create_user_with_defaults(self):
        user = User()
        assert isinstance(user.id, UUID)
        assert isinstance(user.created_at, datetime)
        assert isinstance(user.updated_at, datetime)
        assert user.created_at <= user.updated_at

    def test_create_user_with_explicit_values(self):
        custom_id = uuid4()
        created = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
        updated = datetime(2026, 1, 2, 10, 0, tzinfo=timezone.utc)

        user = User(id=custom_id, created_at=created, updated_at=updated)
        assert user.id == custom_id
        assert user.created_at == created
        assert user.updated_at == updated

    def test_user_equality_and_hash(self):
        common_id = uuid4()
        user1 = User(id=common_id)
        user2 = User(id=common_id)
        user3 = User(id=uuid4())

        assert user1 == user2
        assert user1 != user3
        assert user1 != "not-a-user"
        assert hash(user1) == hash(user2)
        assert {user1, user2} == {user1}

    def test_user_repr(self):
        custom_id = uuid4()
        user = User(id=custom_id)
        assert repr(user) == f"<User id={custom_id}>"

    def test_update_timestamp_default(self):
        created = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
        user = User(created_at=created, updated_at=created)
        initial_updated_at = user.updated_at

        user.update_timestamp()
        assert user.updated_at >= initial_updated_at

    def test_update_timestamp_explicit(self):
        created = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
        user = User(created_at=created, updated_at=created)
        new_timestamp = created + timedelta(days=5)

        user.update_timestamp(new_timestamp)
        assert user.updated_at == new_timestamp


class TestUserValidation:
    """Tests validating User domain invariants and error handling."""

    def test_reject_invalid_user_id(self):
        with pytest.raises(DomainValidationError, match="User id must be a valid UUID"):
            User(id="invalid-uuid")

        with pytest.raises(DomainValidationError, match="User id must be a valid UUID"):
            User(id=12345)

    def test_reject_invalid_created_at(self):
        with pytest.raises(DomainValidationError, match="created_at must be a valid datetime"):
            User(created_at="2026-01-01")

    def test_reject_invalid_updated_at(self):
        with pytest.raises(DomainValidationError, match="updated_at must be a valid datetime"):
            User(updated_at=123456789)

    def test_reject_updated_at_prior_to_created_at(self):
        created = datetime(2026, 2, 1, 10, 0, tzinfo=timezone.utc)
        updated = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)

        with pytest.raises(DomainValidationError, match="updated_at cannot be prior to created_at"):
            User(created_at=created, updated_at=updated)

    def test_reject_update_timestamp_invalid_type(self):
        user = User()
        with pytest.raises(DomainValidationError, match="updated_at must be a valid datetime"):
            user.update_timestamp("invalid-date")

    def test_reject_update_timestamp_prior_to_created_at(self):
        created = datetime(2026, 5, 1, 10, 0, tzinfo=timezone.utc)
        user = User(created_at=created, updated_at=created)
        prior_date = datetime(2026, 4, 1, 10, 0, tzinfo=timezone.utc)

        with pytest.raises(DomainValidationError, match="updated_at cannot be prior to created_at"):
            user.update_timestamp(prior_date)


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__] + sys.argv[1:]))

