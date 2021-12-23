import unittest
from entities.user import User
from services.budget_service import Budget_calculator
from repositories.expense_repository import expense_repository
from repositories.user_repository import user_repository
from entities.expense import Expense

class Test_budget_service(unittest.TestCase):
    def setUp(self):
        expense_repository.clean_sql()
        user_repository.clean_sql()
        self.budget_calc = Budget_calculator()
        self.user_arttu = User('Arttu','123')
        self.expense_arttu = Expense("Arttu","sähkö","35")

    def create_user(self):
        pass

    def login_user(self):
        self.budget_calc.login(self.user_arttu.username, self.user_arttu.password)

    def make_and_login(self):
        username = self.user_arttu.username
        password = self.user_arttu.password

        self.budget_calc.create_account(username, password)

        self.login_user()

    def test_create_user(self):
        username = self.user_arttu.username
        password = self.user_arttu.password

        self.budget_calc.create_account(username, password)

        self.login_user()


        user = self.budget_calc.get_user()

        self.assertEqual(user.username, self.user_arttu.username)

    def test_create_expense(self):
        self.make_and_login()

        self.budget_calc.add_budget(self.expense_arttu.name, self.expense_arttu.content)

        expense = self.budget_calc.get_sum_of_expenses()
        
        self.assertEqual(35, expense)

    def test_delete_expense(self):
        self.make_and_login()

        self.budget_calc.add_budget(self.expense_arttu.name, self.expense_arttu.content)

        self.budget_calc.remove_expense(1)

        self.assertEqual(None ,self.budget_calc.get_sum_of_expenses())