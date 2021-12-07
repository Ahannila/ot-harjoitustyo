import unittest
from repositories.user_repository import user_repository
from entities.user import User

class Test_user_repository(unittest.TestCase):
    def setUp(self):
        user_repository.clean_sql() 
        self.user_arttu = User("Arttu", "NULL")
        self.user_tero = User("Tero", "NULL")

    def test_create(self):
        user_repository.create(self.user_arttu)
        users = user_repository.get_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_arttu.username)

    def test_find_with_username(self):
        user_repository.create(self.user_arttu)

        user = user_repository.find_by_name(self.user_arttu.username)
        self.assertEqual(user.username, self.user_arttu.username)

    def test_find_all(self):
        user_repository.create(self.user_arttu)
        user_repository.create(self.user_tero)

        user = user_repository.get_all_users()

        self.assertEqual(len(user), 2)