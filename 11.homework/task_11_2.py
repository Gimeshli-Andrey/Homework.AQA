import unittest
import logging
from task_11_1 import log_event

class TestLogEvent(unittest.TestCase):
    def setUp(self):
        # Очистка лог-файла перед кожним тестом
        logging.basicConfig(filename='login_system.log', level=logging.INFO)
        logger = logging.getLogger("log_event")
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        open('login_system.log', 'w').close()

    def test_log_success(self):
        log_event('test_user', 'success')
        with open('login_system.log', 'r') as f:
            logs = f.read()
        self.assertIn("Login event - Username: test_user, Status: success", logs)

    def test_log_expired(self):
        log_event('test_user', 'expired')
        with open('login_system.log', 'r') as f:
            logs = f.read()
        self.assertIn("Login event - Username: test_user, Status: expired", logs)

    def test_log_failed(self):
        log_event('test_user', 'failed')
        with open('login_system.log', 'r') as f:
            logs = f.read()
        self.assertIn("Login event - Username: test_user, Status: failed", logs)

if __name__ == '__main__':
    unittest.main()
