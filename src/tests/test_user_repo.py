import unittest
from repositories.user_repository import user_repository
from entities.user import User

class Test_user_repository(unittest.TestCase):
    def setUp(self):
        user_repository.clean_sql() 
        self.user_arttu = User("Arttu", "NULL")

    def test_find_by_name(self):
        user_repository.create(self.user_arttu)
        users = user_repository.find_by_name(self.user_arttu)
        self.assertEqual(users.username, self.user_arttu.username)