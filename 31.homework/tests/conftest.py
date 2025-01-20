import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.registration_page import RegistrationPage

logging.basicConfig(
    filename='test_log.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    logger.info("Запуск драйвера Chrome")
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    logger.info("Закриття драйвера")
    driver.quit()

@pytest.fixture
def auth_url():
    username = "guest"
    password = "welcome2qauto"
    base_url = "qauto2.forstudy.space"
    url = f"https://{username}:{password}@{base_url}"
    logger.info(f"Використання URL для авторизації: {url}")
    return url

@pytest.fixture
def open_registration_page(driver, auth_url):
    logger.info("Відкриття сторінки реєстрації")
    driver.get(auth_url)
    return driver

@pytest.fixture
def registration_page(driver):
    logger.info("Створення об'єкта сторінки реєстрації")
    return RegistrationPage(driver)