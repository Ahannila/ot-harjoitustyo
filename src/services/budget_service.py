from sqlite3.dbapi2 import Connection
from repositories.user_repository import user_repository
from repositories.expense_repository import expense_repository
from database_connection import get_database_connection
from entities.user import User
from entities.expense import Expense


class InvalidCreds(Exception):
    pass

class UserExists(Exception):
    pass


class Budget_calculator():
    def __init__(self):
        self.user = None
        

    def start(self):
        pass


    def login(self, username, password):
        user = user_repository.find_by_name(username)

        if not user or user.password != password:
            #print('Kirjautuminen ei onnistunut')
            raise InvalidCreds('Invalid username or password')
            
        #print("Kirjautuminen onnistui")
        self.user = user
        return user


    def create_account(self, username, password):
        if len(str.strip(username)) == 0 or len(str.strip(password)) == 0:
            raise InvalidCreds('Nothing inserted')

        user = user_repository.create((User(username,password)))
        print("User created")
        return user


    def get_user(self):
        return self.user

    def add_income(self, content):
        pass

    def add_expense(self,content):
        expense = expense_repository.add_expense(self.user.username, content)
        return expense

    def get_expenses(self):
        lista = expense_repository.list_expenses(self.user.username)
        return lista
    
    def get_expense_id(self,expense):
        id = expense_repository.get_expense_id(self.user.username, expense)
        return id

    def get_sum_of_expenses(self):
        sum = expense_repository.get_sum(self.user.username)
        return sum

    def remove_expense(self, id):
        expense_repository.remove_expense(id)


budget_calculator = Budget_calculator()

