from sqlite3.dbapi2 import Connection
from tkinter import ttk, constants
from database_connection import get_database_connection
from entities.user import User

class ExpenseRepository:
    def __init__(self, connection):
        self.connection = get_database_connection()

    def clean_sql(self):
        cursos = self.connection.cursor()

        cursos.execute("DELETE FROM expenses")

        self.connection.commit()

    def add_expense(self, user, content):
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO expenses (username, expense) VALUES (?,?)" [user.username, content])

        self.connection.commit()

        return content

expense_repository = ExpenseRepository(get_database_connection)
