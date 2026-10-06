"""
Income Entity Module.

Specializes FinancialRecord for incoming monetary movements.
"""

from decimal import Decimal

from logic.entities.financial_record import FinancialRecord


class Income(FinancialRecord):
    """
    Concrete financial record representing an income (positive cash flow).
    Inherits all core attributes from FinancialRecord and implements signed_amount().
    """

    type: str = "INCOME"

    def signed_amount(self) -> Decimal:
        """
        Return positive signed amount representing money inflow.
        """
        return +self.amount

