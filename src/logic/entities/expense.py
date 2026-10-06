"""
Expense Entity Module.

Specializes FinancialRecord for outgoing monetary movements.
"""

from decimal import Decimal

from logic.entities.financial_record import FinancialRecord


class Expense(FinancialRecord):
    """
    Concrete financial record representing an expense (negative cash flow).
    Inherits all core attributes from FinancialRecord and implements signed_amount().
    """

    type: str = "EXPENSE"

    def signed_amount(self) -> Decimal:
        """
        Return negative signed amount representing money outflow.
        """
        return -self.amount

