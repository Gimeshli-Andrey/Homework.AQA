import psycopg2
from psycopg2 import Error
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database:
    def __init__(self, host="localhost", database="testdb", user="postgres", password="postgres", port=5432):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            logger.info("Successfully connected to the database")
            return True
        except Error as e:
            logger.error(f"Error connecting to PostgreSQL: {e}")
            return False

    def create_table(self):
        try:
            cursor = self.connection.cursor()
            create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """
            cursor.execute(create_table_query)
            self.connection.commit()
            cursor.close()
            logger.info("Table created successfully")
            return True
        except Error as e:
            logger.error(f"Error creating table: {e}")
            return False

    def insert_user(self, name, email):
        try:
            cursor = self.connection.cursor()
            insert_query = "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id"
            cursor.execute(insert_query, (name, email))
            user_id = cursor.fetchone()[0]
            self.connection.commit()
            cursor.close()
            logger.info(f"User inserted successfully with ID: {user_id}")
            return user_id
        except Error as e:
            logger.error(f"Error inserting user: {e}")
            self.connection.rollback()
            return None

    def update_user(self, user_id, name, email):
        try:
            cursor = self.connection.cursor()
            update_query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
            cursor.execute(update_query, (name, email, user_id))
            rows_affected = cursor.rowcount
            self.connection.commit()
            cursor.close()
            logger.info(f"User {user_id} updated successfully")
            return rows_affected > 0
        except Error as e:
            logger.error(f"Error updating user: {e}")
            self.connection.rollback()
            return False

    def delete_user(self, user_id):
        try:
            cursor = self.connection.cursor()
            delete_query = "DELETE FROM users WHERE id = %s"
            cursor.execute(delete_query, (user_id,))
            rows_affected = cursor.rowcount
            self.connection.commit()
            cursor.close()
            logger.info(f"User {user_id} deleted successfully")
            return rows_affected > 0
        except Error as e:
            logger.error(f"Error deleting user: {e}")
            self.connection.rollback()
            return False

    def get_all_users(self):
        try:
            cursor = self.connection.cursor()
            select_query = "SELECT id, name, email, created_at FROM users"
            cursor.execute(select_query)
            users = cursor.fetchall()
            cursor.close()
            return users
        except Error as e:
            logger.error(f"Error getting users: {e}")
            return []

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed")