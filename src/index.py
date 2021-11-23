from sqlite3.dbapi2 import Connection
from user_repository import user_repository
from database_connection import get_database_connection

class Budget_calculator():
    def __init__(self, connection):
        self.user = None
        self._connection = connection

    def start(self):
        print("Welcome to budget-tracker 9000")
        print("Commands")
        print("1: LOGIN")
        print("2: CREATE ACCOUNT")

        while True:
            command = input("Choose command: ")


            if command == "1":
                self.login()
            elif command == "2":
                self.create_account()
            elif self.user!=None:
                print("Welcome in!")
            else:
                print("No such command")


    def login(self):
        username = input("Enter username: ")
        user = user_repository.find_by_name(username)

        if not user:
            print("User not found")
            return 
        
        self.user = user    
        return user


    def create_account(self):
        name = input("Enter nick: ")
        user_repository.create(name)

app = Budget_calculator(Connection)
app.start()