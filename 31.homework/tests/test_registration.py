import logging
import os
import random
import string
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.registration_page import RegistrationPage
import time
import allure

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
fake = Faker()

def generate_random_password(length=10):
    if length < 8 or length > 15:
        raise ValueError("Password length must be between 8 and 15 characters.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    password += random.choices(lower + upper + digits, k=length - 3)
    random.shuffle(password)

    return ''.join(password)

def take_screenshot(driver, name="screenshot"):
    screenshot_path = os.path.join(os.getcwd(), f"{name}_{int(time.time())}.png")
    driver.save_screenshot(screenshot_path)
    logger.error(f"Скриншот збережено: {screenshot_path}")

@allure.feature('User  Registration')
@allure.story('Successful Registration')
def test_user_registration(open_registration_page, registration_page):
    driver = open_registration_page

    try:
        logger.info("Натискаємо кнопку 'Sign up'")
        sign_up_button = driver.find_element(By.XPATH,
                                             "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/button")
        sign_up_button.click()

        logger.info("Очікуємо, поки з'явиться форма реєстрації")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "signupName"))
        )

        random_name = fake.first_name()
        random_last_name = fake.last_name()
        random_email = fake.email()
        random_password = generate_random_password(10)

        logger.info(f"Генеруємо дані: Name: {random_name}, Last Name: {random_last_name}, Email: {random_email}, Password: {random_password}")

        logger.info("Заповнюємо форму реєстрації")
        registration_page.enter_name(random_name)
        registration_page.enter_last_name(random_last_name)
        registration_page.enter_email(random_email)
        registration_page.enter_password(random_password)
        registration_page.repeat_password(random_password)

        logger.info("Перевіряємо, чи кнопка 'Register' активна")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(registration_page.REGISTER_BUTTON)
        )

        logger.info("Клік на кнопку реєстрації")
        registration_page.click_register_button()

        logger.info("Перевірка на успішну реєстрацію")
        WebDriverWait(driver, 10).until(
            EC.url_contains("/panel/garage")
        )

        assert "/panel/garage" in driver.current_url, "Реєстрація не була успішною."

    except Exception as e:
        logger.error(f"Помилка під час тестування: {str(e)}")
        take_screenshot(driver, "registration_error")
        raise