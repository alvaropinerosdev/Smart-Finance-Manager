"""
Unit tests for User and Category entities.
"""

from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid4

import pytest

from exceptions import DomainValidationError
from logic.entities import Category, User


@pytest.fixture
def sample_user_id() -> UUID:
    return uuid4()


@pytest.fixture
def sample_category_id() -> UUID:
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


class TestCategoryEntity:
    """Tests verifying Category entity lifecycle and behavior."""

    def test_create_category_with_required_fields(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        category = Category(
            id=sample_category_id,
            user_id=sample_user_id,
            name="Groceries",
            type="EXPENSE",
            is_default=True,
            created_at=sample_created_at,
        )
        assert category.id == sample_category_id
        assert category.user_id == sample_user_id
        assert category.name == "Groceries"
        assert category.type == "EXPENSE"
        assert category.is_default is True
        assert category.created_at == sample_created_at
        assert category.updated_at == sample_created_at
        assert category.deleted_at is None
        assert category.is_active() is True

    def test_create_category_with_explicit_updated_and_deleted_at(
        self,
        sample_category_id: UUID,
        sample_user_id: UUID,
        sample_created_at: datetime,
        sample_updated_at: datetime,
    ):
        deleted_date = sample_created_at + timedelta(days=2)
        category = Category(
            id=sample_category_id,
            user_id=sample_user_id,
            name="Salary",
            type="INCOME",
            is_default=False,
            created_at=sample_created_at,
            updated_at=sample_updated_at,
            deleted_at=deleted_date,
        )
        assert category.is_default is False
        assert category.updated_at == sample_updated_at
        assert category.deleted_at == deleted_date
        assert category.is_active() is False

    def test_category_rename_success(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        category = Category(
            id=sample_category_id,
            user_id=sample_user_id,
            name="Food",
            type="EXPENSE",
            is_default=True,
            created_at=sample_created_at,
        )
        initial_updated_at = category.updated_at

        category.rename("Dining Out")
        assert category.name == "Dining Out"
        assert category.updated_at >= initial_updated_at

    def test_category_accepts(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        expense_cat = Category(
            id=sample_category_id,
            user_id=sample_user_id,
            name="Rent",
            type="EXPENSE",
            is_default=True,
            created_at=sample_created_at,
        )
        income_cat = Category(
            id=uuid4(),
            user_id=sample_user_id,
            name="Investments",
            type="INCOME",
            is_default=True,
            created_at=sample_created_at,
        )

        assert expense_cat.accepts("EXPENSE") is True
        assert expense_cat.accepts("expense") is True
        assert expense_cat.accepts("  EXPENSE  ") is True
        assert expense_cat.accepts("INCOME") is False
        assert expense_cat.accepts(123) is False  # type: ignore

        assert income_cat.accepts("INCOME") is True
        assert income_cat.accepts("income") is True
        assert income_cat.accepts("EXPENSE") is False

    def test_category_soft_delete(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        category = Category(
            id=sample_category_id,
            user_id=sample_user_id,
            name="Entertainment",
            type="EXPENSE",
            is_default=True,
            created_at=sample_created_at,
        )
        assert category.is_active() is True
        assert category.deleted_at is None

        category.soft_delete()
        assert category.is_active() is False
        assert isinstance(category.deleted_at, datetime)
        assert category.updated_at == category.deleted_at

    def test_category_equality_and_hash(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        cat1 = Category(
            id=sample_category_id,
            user_id=sample_user_id,
            name="Cat1",
            type="INCOME",
            is_default=True,
            created_at=sample_created_at,
        )
        cat2 = Category(
            id=sample_category_id,
            user_id=sample_user_id,
            name="Cat2",
            type="INCOME",
            is_default=True,
            created_at=sample_created_at,
        )
        cat3 = Category(
            id=uuid4(),
            user_id=sample_user_id,
            name="Cat1",
            type="INCOME",
            is_default=True,
            created_at=sample_created_at,
        )

        assert cat1 == cat2
        assert cat1 != cat3
        assert cat1 != "not-a-category"
        assert hash(cat1) == hash(cat2)
        assert {cat1, cat2} == {cat1}

    def test_category_repr(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        category = Category(
            id=sample_category_id,
            user_id=sample_user_id,
            name="Utilities",
            type="EXPENSE",
            is_default=True,
            created_at=sample_created_at,
        )
        assert repr(category) == (
            f"<Category id={sample_category_id} name='Utilities' type='EXPENSE' active=True>"
        )


class TestCategoryValidation:
    """Tests validating Category domain invariants and error handling."""

    def test_cannot_instantiate_category_without_required_fields(self):
        with pytest.raises(TypeError):
            Category()  # type: ignore

    def test_cannot_instantiate_category_with_missing_arguments(
        self, sample_category_id: UUID, sample_user_id: UUID
    ):
        with pytest.raises(TypeError):
            Category(id=sample_category_id, user_id=sample_user_id)  # type: ignore

    def test_reject_invalid_ids(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        with pytest.raises(DomainValidationError, match="Category id must be a valid UUID"):
            Category(
                id="not-a-uuid",  # type: ignore
                user_id=sample_user_id,
                name="Test",
                type="INCOME",
                is_default=True,
                created_at=sample_created_at,
            )

        with pytest.raises(DomainValidationError, match="user_id must be a valid UUID"):
            Category(
                id=sample_category_id,
                user_id=12345,  # type: ignore
                name="Test",
                type="INCOME",
                is_default=True,
                created_at=sample_created_at,
            )

    def test_reject_invalid_name(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        with pytest.raises(DomainValidationError, match="Category name must be a string"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name=123,  # type: ignore
                type="INCOME",
                is_default=True,
                created_at=sample_created_at,
            )

        with pytest.raises(DomainValidationError, match="Category name cannot be empty or blank"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name="",
                type="INCOME",
                is_default=True,
                created_at=sample_created_at,
            )

        with pytest.raises(DomainValidationError, match="Category name cannot be empty or blank"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name="     ",
                type="INCOME",
                is_default=True,
                created_at=sample_created_at,
            )

        with pytest.raises(DomainValidationError, match="Category name cannot exceed 100 characters"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name="A" * 101,
                type="INCOME",
                is_default=True,
                created_at=sample_created_at,
            )

    def test_reject_rename_invalid_name(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        category = Category(
            id=sample_category_id,
            user_id=sample_user_id,
            name="Valid",
            type="INCOME",
            is_default=True,
            created_at=sample_created_at,
        )

        with pytest.raises(DomainValidationError, match="Category name cannot be empty or blank"):
            category.rename("")

        with pytest.raises(DomainValidationError, match="Category name cannot be empty or blank"):
            category.rename("   ")

        with pytest.raises(DomainValidationError, match="Category name cannot exceed 100 characters"):
            category.rename("X" * 101)

    def test_reject_invalid_type(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        with pytest.raises(DomainValidationError, match="Category type must be a string"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name="Test",
                type=123,  # type: ignore
                is_default=True,
                created_at=sample_created_at,
            )

        with pytest.raises(DomainValidationError, match="Must be 'INCOME' or 'EXPENSE'"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name="Test",
                type="INVALID_TYPE",
                is_default=True,
                created_at=sample_created_at,
            )

    def test_reject_invalid_is_default(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        with pytest.raises(DomainValidationError, match="is_default must be a boolean"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name="Test",
                type="INCOME",
                is_default="true",  # type: ignore
                created_at=sample_created_at,
            )

    def test_reject_invalid_datetimes(
        self, sample_category_id: UUID, sample_user_id: UUID, sample_created_at: datetime
    ):
        with pytest.raises(DomainValidationError, match="created_at must be a valid datetime"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name="Test",
                type="INCOME",
                is_default=True,
                created_at="invalid-date",  # type: ignore
            )

        with pytest.raises(DomainValidationError, match="updated_at must be a valid datetime"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name="Test",
                type="INCOME",
                is_default=True,
                created_at=sample_created_at,
                updated_at="invalid-date",  # type: ignore
            )

        with pytest.raises(DomainValidationError, match="deleted_at must be a valid datetime"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name="Test",
                type="INCOME",
                is_default=True,
                created_at=sample_created_at,
                deleted_at="invalid-date",  # type: ignore
            )

        prior_date = sample_created_at - timedelta(days=1)
        with pytest.raises(DomainValidationError, match="updated_at cannot be prior to created_at"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name="Test",
                type="INCOME",
                is_default=True,
                created_at=sample_created_at,
                updated_at=prior_date,
            )

        with pytest.raises(DomainValidationError, match="deleted_at cannot be prior to created_at"):
            Category(
                id=sample_category_id,
                user_id=sample_user_id,
                name="Test",
                type="INCOME",
                is_default=True,
                created_at=sample_created_at,
                deleted_at=prior_date,
            )


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__] + sys.argv[1:]))
