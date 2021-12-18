from sqlite3.dbapi2 import Cursor
from database_connection import get_database_connection
from entities.expense import Expense

def get_expense_by_row(row):
    return row[0] if row else None

def get_whole_expense_by_row(row):
    return Expense(row['username'], row['expense_name'], row['content']) if row else None

class ExpenseRepository:
    def __init__(self, connection):
        self.connection = get_database_connection()

    def clean_sql(self):
        """Poistaa kaiken tiedon Tietokannasta.
        """


        cursos = self.connection.cursor()

        cursos.execute("DELETE FROM expenses")

        self.connection.commit()


    def add_expense(self, budget):
        """Lisää tietokantaan kulun
        
        Args:
            user: Käyttäjän username, joka tallennetaan tietokantaan.
            content: Kulun määrä joka tallennetaan INTEGER-muodossa tietokantaan.
        """
        
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO expenses (username, name, expense) VALUES (?,?,?)", [budget.username, budget.name, budget.content])

        self.connection.commit()

        return budget


    def get_expense_as_entity(self, id, username, content):
        cursor = self.connection.cursor()

        cursor.execute("SELECT id, username, name, expense FROM expenses where (id,username,expense) = (?,?,?)", [id, username, content])

        row = cursor.fetchone()

        return get_whole_expense_by_row(row)

    def get_expense_id(self,user,content):
        cursor = self.connection.cursor()

        cursor.execute("SELECT id FROM expenses WHERE (username,expense) = (?,?)", [user,content])

        row = cursor.fetchone()

        return get_expense_by_row(row)

    def get_expense_name_with_id(self, id):
        cursos = self.connection.cursor()

        cursos.execute("SELECT name FROM expenses WHERE id= ?",[id])

        row = cursos.fetchone()

        return get_expense_by_row(row)

    def remove_expense(self, id):
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM expenses WHERE id = ?", [id])

        self.connection.commit()

        return


    def list_expenses(self, user):
        cursor = self.connection.cursor()

        cursor.execute("SELECT expense FROM expenses WHERE username = ?", [user])

        row = cursor.fetchall()

        return list(map(get_expense_by_row, row))


    def get_sum(self, user):
        cursor = self.connection.cursor()

        cursor.execute("SELECT SUM(expense) FROM expenses WHERE username = ?",[user])

        row = cursor.fetchone()

        return get_expense_by_row(row)

expense_repository = ExpenseRepository(get_database_connection)
