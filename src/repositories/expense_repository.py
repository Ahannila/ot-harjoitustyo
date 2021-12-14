from sqlite3.dbapi2 import Connection
from tkinter import ttk, constants
from database_connection import get_database_connection
from entities.user import User
from entities.expense import Expense

def get_expense_by_row(row):
    return row[0] if row else None

class ExpenseRepository:
    def __init__(self, connection):
        self.connection = get_database_connection()

    def clean_sql(self):
        cursos = self.connection.cursor()

        cursos.execute("DELETE FROM expenses")

        self.connection.commit()

    def add_expense(self, user, content):
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO expenses (username, expense) VALUES (?,?)", [user, content])

        self.connection.commit()

        return content

    def list_expenses(self, user):
        cursor = self.connection.cursor()
        cursor.execute("SELECT expense FROM expenses WHERE username = ?", [user])
        row = cursor.fetchall()
        return list(map(get_expense_by_row, row))

expense_repository = ExpenseRepository(get_database_connection)
