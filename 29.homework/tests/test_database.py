import unittest
import os
from src.database import Database


class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = Database(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME', 'testdb'),
            user=os.getenv('DB_USER', 'postgres'),
            password=os.getenv('DB_PASSWORD', 'postgres'),
            port=int(os.getenv('DB_PORT', 5432))
        )
        cls.db.connect()

    def setUp(self):
        self.db.create_table()

    def tearDown(self):
        if self.db.connection:
            cursor = self.db.connection.cursor()
            cursor.execute("DELETE FROM users")
            self.db.connection.commit()
            cursor.close()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def test_connection(self):
        self.assertTrue(self.db.connection is not None)

    def test_insert_user(self):
        user_id = self.db.insert_user("Test User", "test@example.com")
        self.assertIsNotNone(user_id)
        users = self.db.get_all_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], "Test User")

    def test_update_user(self):
        user_id = self.db.insert_user("Test User", "test@example.com")
        updated = self.db.update_user(user_id, "Updated User", "updated@example.com")
        self.assertTrue(updated)
        users = self.db.get_all_users()
        self.assertEqual(users[0][1], "Updated User")
        self.assertEqual(users[0][2], "updated@example.com")

    def test_delete_user(self):
        user_id = self.db.insert_user("Test User", "test@example.com")
        deleted = self.db.delete_user(user_id)
        self.assertTrue(deleted)
        users = self.db.get_all_users()
        self.assertEqual(len(users), 0)

    def test_get_all_users(self):
        test_users = [
            ("User 1", "user1@example.com"),
            ("User 2", "user2@example.com"),
            ("User 3", "user3@example.com")
        ]
        for name, email in test_users:
            self.db.insert_user(name, email)

        users = self.db.get_all_users()
        self.assertEqual(len(users), 3)


if __name__ == '__main__':
    unittest.main()