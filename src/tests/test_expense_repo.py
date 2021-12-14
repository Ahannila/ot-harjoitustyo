import unittest
from repositories.expense_repository import expense_repository
from entities.expense import Expense

class Test_expense_repository(unittest.TestCase):
    def setUp(self):
        expense_repository.clean_sql()
        self.expense_100 = Expense("arttu", 100)
        self.expense_50 = Expense('Tero', 50)

    def test_add_expense(self):
        expense_repository.add_expense(self.expense_100.username, self.expense_100.content)
        expenses = expense_repository.list_expenses(self.expense_100.username)

        self.assertEqual(len(expenses),1)
        self.assertEqual(expenses[0], self.expense_100.content)
        