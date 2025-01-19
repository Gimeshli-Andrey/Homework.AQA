import pytest
import allure
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.pages.registration_page import RegistrationPage
from src.pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def fake_user():
    fake = Faker('uk_UA')
    return {
        'firstname': fake.first_name(),
        'lastname': fake.last_name(),
        'email': fake.email(),
        'phone': f'+380{fake.msisdn()[3:]}',
        'password': fake.password(length=12)
    }


@allure.epic("NCASE Website Testing")
@allure.feature("User Registration and Authentication")
class TestNCASE:

    @allure.story("User Registration")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_registration(self, driver, fake_user):
        with allure.step("Navigate to registration page"):
            driver.get("https://ncase.ua/create-account")
            registration_page = RegistrationPage(driver)

        with allure.step("Fill registration form"):
            registration_page.fill_registration_form(fake_user)

        with allure.step("Submit registration"):
            registration_page.click_register()

        assert "account" in driver.current_url

    @allure.story("User Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, driver, fake_user):
        with allure.step("Navigate to login page"):
            driver.get("https://ncase.ua")
            login_page = LoginPage(driver)

        with allure.step("Perform login"):
            login_page.login(fake_user['email'], fake_user['password'])

        assert "account" in driver.current_url