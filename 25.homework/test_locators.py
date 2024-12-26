import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators import xpath_locators, css_locators

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_results.log")
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def get_driver():
    try:
        return webdriver.Safari()
    except Exception as e:
        logger.error(f"Error initializing the driver: {str(e)}")
        raise

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    yield driver
    driver.quit()

def check_locator(driver, locator, locator_type):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((locator_type, locator))
        )
        return True
    except TimeoutException:
        logger.warning(f"Locator not found: {locator} of type {locator_type}")
        return False

def log_locator_result(locator_type, number, found):
    if found:
        logger.info(f"{locator_type} локатор {number}: Знайдено")
    else:
        logger.info(f"{locator_type} локатор {number}: Не знайдено")

def test_locators(driver):
    xpath_found = 0
    xpath_not_found = 0
    css_found = 0
    css_not_found = 0

    logger.info("Перевірка XPath локаторів:")
    for number, xpath in xpath_locators.items():
        found = check_locator(driver, xpath, By.XPATH)
        log_locator_result("XPath", number, found)
        if found:
            xpath_found += 1
        else:
            xpath_not_found += 1

    logger.info("\nПеревірка CSS локаторів:")
    for number, css in css_locators.items():
        found = check_locator(driver, css, By.CSS_SELECTOR)
        log_locator_result("CSS", number, found)
        if found:
            css_found += 1
        else:
            css_not_found += 1

    logger.info("\n--- Результати перевірки ---")
    logger.info(f"XPath локаторів знайдено: {xpath_found}, не знайдено: {xpath_not_found}")
    logger.info(f"CSS локаторів знайдено: {css_found}, не знайдено: {css_not_found}")

if __name__ == "__main__":
    pytest.main()