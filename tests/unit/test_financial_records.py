"""
Unit tests for FinancialRecord, Income, and Expense entities.
"""

from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID, uuid4

import pytest

from exceptions import DomainValidationError
from logic.entities import FinancialRecord, Income, Expense


@pytest.fixture
def sample_user_id() -> UUID:
    return uuid4()


@pytest.fixture
def sample_category_id() -> UUID:
    return uuid4()


@pytest.fixture
def sample_datetime() -> datetime:
    return datetime(2026, 10, 5, 12, 0, tzinfo=timezone.utc)


class TestFinancialRecordABC:
    """Tests ensuring FinancialRecord behaves as an abstract base class."""

    def test_cannot_instantiate_abstract_base_class(
        self, sample_user_id: UUID, sample_category_id: UUID, sample_datetime: datetime
    ):
        """FinancialRecord is abstract and cannot be instantiated directly."""
        with pytest.raises(TypeError, match="Can't instantiate abstract class"):
            FinancialRecord(
                user_id=sample_user_id,
                category_id=sample_category_id,
                amount=Decimal("100.00"),
                currency="USD",
                transaction_datetime=sample_datetime,
            )


class TestIncomeEntity:
    """Tests verifying Income entity behavior and signed amount."""

    def test_create_income_success(
        self, sample_user_id: UUID, sample_category_id: UUID, sample_datetime: datetime
    ):
        income = Income(
            user_id=sample_user_id,
            category_id=sample_category_id,
            amount=Decimal("2500.50"),
            currency="USD",
            transaction_datetime=sample_datetime,
            description="Monthly salary",
            payment_method="Direct Deposit",
            location="Remote",
        )

        assert isinstance(income.id, UUID)
        assert income.user_id == sample_user_id
        assert income.category_id == sample_category_id
        assert income.type == "INCOME"
        assert income.amount == Decimal("2500.50")
        assert income.currency == "USD"
        assert income.transaction_datetime == sample_datetime
        assert income.description == "Monthly salary"
        assert income.payment_method == "Direct Deposit"
        assert income.location == "Remote"
        assert isinstance(income.created_at, datetime)
        assert isinstance(income.updated_at, datetime)
        assert income.deleted_at is None

    def test_income_signed_amount_is_positive(
        self, sample_user_id: UUID, sample_category_id: UUID, sample_datetime: datetime
    ):
        income = Income(
            user_id=sample_user_id,
            category_id=sample_category_id,
            amount=Decimal("350.00"),
            currency="USD",
            transaction_datetime=sample_datetime,
        )

        assert income.signed_amount() == Decimal("350.00")
        assert income.signed_amount() > Decimal("0")


class TestExpenseEntity:
    """Tests verifying Expense entity behavior and signed amount."""

    def test_create_expense_success(
        self, sample_user_id: UUID, sample_category_id: UUID, sample_datetime: datetime
    ):
        expense = Expense(
            user_id=sample_user_id,
            category_id=sample_category_id,
            amount=Decimal("45.75"),
            currency="eur",
            transaction_datetime=sample_datetime,
            description="Groceries",
            payment_method="Credit Card",
            location="Supermarket",
        )

        assert isinstance(expense.id, UUID)
        assert expense.user_id == sample_user_id
        assert expense.category_id == sample_category_id
        assert expense.type == "EXPENSE"
        assert expense.amount == Decimal("45.75")
        assert expense.currency == "EUR"  # Normalized to uppercase
        assert expense.description == "Groceries"
        assert expense.payment_method == "Credit Card"
        assert expense.location == "Supermarket"

    def test_expense_signed_amount_is_negative(
        self, sample_user_id: UUID, sample_category_id: UUID, sample_datetime: datetime
    ):
        expense = Expense(
            user_id=sample_user_id,
            category_id=sample_category_id,
            amount=Decimal("80.00"),
            currency="USD",
            transaction_datetime=sample_datetime,
        )

        assert expense.signed_amount() == Decimal("-80.00")
        assert expense.signed_amount() < Decimal("0")


class TestFinancialRecordValidation:
    """Tests verifying validation invariants on financial records."""

    def test_reject_zero_or_negative_amount(
        self, sample_user_id: UUID, sample_category_id: UUID, sample_datetime: datetime
    ):
        with pytest.raises(DomainValidationError, match="strictly positive"):
            Income(
                user_id=sample_user_id,
                category_id=sample_category_id,
                amount=Decimal("0.00"),
                currency="USD",
                transaction_datetime=sample_datetime,
            )

        with pytest.raises(DomainValidationError, match="strictly positive"):
            Expense(
                user_id=sample_user_id,
                category_id=sample_category_id,
                amount=Decimal("-15.00"),
                currency="USD",
                transaction_datetime=sample_datetime,
            )

    def test_reject_non_decimal_amount(
        self, sample_user_id: UUID, sample_category_id: UUID, sample_datetime: datetime
    ):
        with pytest.raises(DomainValidationError, match="instance of Decimal"):
            Income(
                user_id=sample_user_id,
                category_id=sample_category_id,
                amount=100.0,  # float
                currency="USD",
                transaction_datetime=sample_datetime,
            )

    @pytest.mark.parametrize("invalid_currency", ["US", "USDT", "123", "$$$", "", "   "])
    def test_reject_invalid_currency(
        self,
        sample_user_id: UUID,
        sample_category_id: UUID,
        sample_datetime: datetime,
        invalid_currency: str,
    ):
        with pytest.raises(DomainValidationError, match="ISO 4217"):
            Income(
                user_id=sample_user_id,
                category_id=sample_category_id,
                amount=Decimal("50.00"),
                currency=invalid_currency,
                transaction_datetime=sample_datetime,
            )

    def test_reject_invalid_ids(self, sample_user_id: UUID, sample_datetime: datetime):
        with pytest.raises(DomainValidationError, match="user_id must be a valid UUID"):
            Income(
                user_id="invalid-uuid",
                category_id=uuid4(),
                amount=Decimal("50.00"),
                currency="USD",
                transaction_datetime=sample_datetime,
            )

        with pytest.raises(DomainValidationError, match="category_id must be a valid UUID"):
            Income(
                user_id=sample_user_id,
                category_id=12345,
                amount=Decimal("50.00"),
                currency="USD",
                transaction_datetime=sample_datetime,
            )

        with pytest.raises(DomainValidationError, match="id must be a valid UUID"):
            Income(
                user_id=sample_user_id,
                category_id=uuid4(),
                amount=Decimal("50.00"),
                currency="USD",
                transaction_datetime=sample_datetime,
                id="not-a-uuid",
            )

    def test_reject_invalid_datetime(
        self, sample_user_id: UUID, sample_category_id: UUID
    ):
        with pytest.raises(DomainValidationError, match="valid datetime instance"):
            Expense(
                user_id=sample_user_id,
                category_id=sample_category_id,
                amount=Decimal("20.00"),
                currency="USD",
                transaction_datetime="2026-10-05",  # string instead of datetime
            )

    def test_reject_non_string_currency(
        self, sample_user_id: UUID, sample_category_id: UUID, sample_datetime: datetime
    ):
        with pytest.raises(DomainValidationError, match="Currency must be a string"):
            Income(
                user_id=sample_user_id,
                category_id=sample_category_id,
                amount=Decimal("50.00"),
                currency=12345,  # int
                transaction_datetime=sample_datetime,
            )

    def test_reject_non_string_type(
        self, sample_user_id: UUID, sample_category_id: UUID, sample_datetime: datetime
    ):
        with pytest.raises(DomainValidationError, match="Type must be a string"):
            Income(
                user_id=sample_user_id,
                category_id=sample_category_id,
                amount=Decimal("50.00"),
                currency="USD",
                transaction_datetime=sample_datetime,
                type=123,  # int
            )

    def test_reject_subclass_without_type(
        self, sample_user_id: UUID, sample_category_id: UUID, sample_datetime: datetime
    ):
        class RecordWithoutType(FinancialRecord):
            def signed_amount(self) -> Decimal:
                return self.amount

        with pytest.raises(DomainValidationError, match="Record type must be defined"):
            RecordWithoutType(
                user_id=sample_user_id,
                category_id=sample_category_id,
                amount=Decimal("50.00"),
                currency="USD",
                transaction_datetime=sample_datetime,
            )
