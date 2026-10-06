"""
Entities package exposing domain models for Smart Finance Manager.
"""

from logic.entities.financial_record import FinancialRecord
from logic.entities.income import Income
from logic.entities.expense import Expense

__all__ = [
    "FinancialRecord",
    "Income",
    "Expense",
]

