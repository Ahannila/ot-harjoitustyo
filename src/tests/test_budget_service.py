import unittest
from entities.user import User
from services.budget_service import Budget_calculator
from repositories.expense_repository import expense_repository
from repositories.user_repository import user_repository
from entities import expense

class Test_budget_service(unittest.TestCase):
    def setUp(self):
        expense_repository.clean_sql()
        user_repository.clean_sql()
        self.budget_calc = Budget_calculator()
        self.user_arttu = User('Arttu','123')

    def create_user(self):
        pass

    def login_user(self):
        self.budget_calc.login(self.user_arttu.username, self.user_arttu.password)

    def test_create_user(self):
        username = self.user_arttu.username
        password = self.user_arttu.password

        self.budget_calc.create_account(username, password)

        self.login_user()


        user = self.budget_calc.get_user()

        self.assertEqual(user.username, self.user_arttu.username)