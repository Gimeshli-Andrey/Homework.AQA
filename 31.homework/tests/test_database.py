import os
import pytest
import allure
from src.database import Database

@pytest.fixture(scope="module")
def db():
    db_instance = Database(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'testdb'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'postgres'),
        port=int(os.getenv('DB_PORT', 5432))
    )
    db_instance.connect()
    yield db_instance
    db_instance.close()

@pytest.fixture(autouse=True)
def create_table(db):
    db.create_table()

    yield
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM users")
    db.connection.commit()
    cursor.close()

@allure.feature('Database Operations')
def test_connection(db):
    with allure.step("Testing the database connection"):
        assert db.connection is not None

@allure.feature('Database Operations')
def test_insert_user(db):
    with allure.step("Inserting a test user into the database"):
        user_id = db.insert_user("Test User", "test@example.com")
        assert user_id is not None
        users = db.get_all_users()
        assert len(users) == 1
        assert users[0][1] == "Test User"

@allure.feature('Database Operations')
def test_update_user(db):
    with allure.step("Updating a test user in the database"):
        user_id = db.insert_user("Test User", "test@example.com")
        updated = db.update_user(user_id, "Updated User", "updated@example.com")
        assert updated
        users = db.get_all_users()
        assert users[0][1] == "Updated User"
        assert users[0][2] == "updated@example.com"

@allure.feature('Database Operations')
def test_delete_user(db):
    with allure.step("Deleting a test user from the database"):
        user_id = db.insert_user("Test User", "test@example.com")
        deleted = db.delete_user(user_id)
        assert deleted
        users = db.get_all_users()
        assert len(users) == 0

@allure.feature('Database Operations')
def test_get_all_users(db):
    with allure.step("Retrieving all users from the database"):
        test_users = [
            ("User 1", "user1@example.com"),
            ("User 2", "user2@example.com"),
            ("User 3", "user3@example.com")
        ]
        for name, email in test_users:
            db.insert_user(name, email)
        users = db.get_all_users()
        assert len(users) == 3