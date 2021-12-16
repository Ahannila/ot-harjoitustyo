from database_connection import get_database_connection

def get_expense_by_row(row):
    return row[0] if row else None

class ExpenseRepository:
    def __init__(self, connection):
        self.connection = get_database_connection()

    def clean_sql(self):
        """Poistaa kaiken tiedon Tietokannasta.
        """


        cursos = self.connection.cursor()

        cursos.execute("DELETE FROM expenses")

        self.connection.commit()


    def add_expense(self, user, content):
        """Lisää tietokantaan kulun
        
        Args:
            user: Käyttäjän username, joka tallennetaan tietokantaan.
            content: Kulun määrä joka tallennetaan INTEGER-muodossa tietokantaan.
        """


        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO expenses (username, expense) VALUES (?,?)", [user, content])

        self.connection.commit()

        return content


    def get_expense_id(self,user,content):
        cursor = self.connection.cursor()

        cursor.execute("SELECT id FROM expenses WHERE (username,expense) = (?,?)", [user,content])

        row = cursor.fetchone()

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
