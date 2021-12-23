import unittest
from repositories.expense_repository import expense_repository
from entities.expense import Expense

class Test_expense_repository(unittest.TestCase):
    def setUp(self):
        expense_repository.clean_sql()
        self.expense_100 = Expense("arttu","", 100)
        self.expense_75 = Expense("Jony" ,"sähkö", 15)
        self.expense_50 = Expense('Tero', "" , 50)

    def test_add_expense(self):
        expense_repository.add_expense(self.expense_100)
        expenses = expense_repository.list_expenses(self.expense_100.username)

        self.assertEqual(len(expenses),1)
        self.assertEqual(expenses[0], self.expense_100.content)
        
    def test_get_expense_id(self):
        expense_repository.add_expense(self.expense_100)

        expense_id = expense_repository.get_expense_id(self.expense_100.username, self.expense_100.content)

        self.assertEqual(1, expense_id)

    def test_get_name_with_id(self):
        expense_repository.add_expense(self.expense_75)

        expense_id = expense_repository.get_expense_id(self.expense_75.username, self.expense_75.content)
        expense_name = expense_repository.get_expense_name_with_id(expense_id)

        self.assertEqual(expense_name, self.expense_75.name)