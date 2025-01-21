import os
import logging
from src.database import Database

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    db = Database(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'testdb'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'postgres'),
        port=int(os.getenv('DB_PORT', 5432))
    )

    try:
        if not db.connect():
            logger.error("Failed to connect to the database")
            return

        if not db.create_table():
            logger.error("Failed to create table")
            return

        logger.info("Adding test users...")
        test_users = [
            ("John Doe", "john@example.com"),
            ("Jane Smith", "jane@example.com"),
            ("Bob Wilson", "bob@example.com")
        ]

        user_ids = []
        for name, email in test_users:
            user_id = db.insert_user(name, email)
            if user_id:
                user_ids.append(user_id)
                logger.info(f"Added user {name} with ID: {user_id}")

        logger.info("Current users in database:")
        users = db.get_all_users()
        for user in users:
            logger.info(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Created: {user[3]}")

        if user_ids:
            logger.info("Updating first user...")
            if db.update_user(user_ids[0], "John Updated", "john.updated@example.com"):
                logger.info("First user updated successfully")

        if len(user_ids) > 2:
            logger.info("Deleting last user...")
            if db.delete_user(user_ids[-1]):
                logger.info("Last user deleted successfully")

        logger.info("Final user list:")
        users = db.get_all_users()
        for user in users:
            logger.info(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Created: {user[3]}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()