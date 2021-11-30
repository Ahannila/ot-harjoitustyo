
from sqlite3.dbapi2 import Cursor
from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row['username']) if row else None


class UserRepository:

    def __init__(self, connection):
        self._connection = get_database_connection()

    def clean_sql(self):
        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM users')

        self._connection.commit()

    def find_by_name(self, user):  # palauttaa käyttäjän kirjautuessa
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", [user])

        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):  # Tekee uuden käyttäjän.
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO users (username) VALUES (?)", [user])

        self._connection.commit()

        return user


user_repository = UserRepository(get_database_connection())
