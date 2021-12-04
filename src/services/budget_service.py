from sqlite3.dbapi2 import Connection
from repositories.user_repository import user_repository
from database_connection import get_database_connection
from entities.user import User


class InvalidCreds(Exception):
    pass


class Budget_calculator():
    def __init__(self, connection):
        self.user = None
        self._connection = connection

    def start(self):
        pass
#        print("Welcome to budget-tracker 9000")
#        print("Commands")
#        print("X: SUSPEND")
#        print("1: LOGIN")
#        print("2: CREATE ACCOUNT")
#
#        while True:
#            command = input("Choose command: ")
#

#            if command == "1":
#                self.login()
#            elif command == "2":
#                self.create_account()
#            elif command == "X":
#                break
#            elif self.user!=None:
#                print("Welcome in!")
#            else:
#                print("No such command")

    def login(self, username):
        user = user_repository.find_by_name(username)

        if not user:
            print('Kirjautuminen ei onnistunut')
            raise InvalidCreds('Invalid username')
            
        print("Kirjautuminen onnistui")
        self.user = user
        return user

    def create_account(self, username, password):
        user = user_repository.create((User(username,password)))
        print("User created")
        return user


    def add_income(self, content):
        pass

    def add_expense(self, content):
        pass


app = Budget_calculator(Connection)
app.start()
