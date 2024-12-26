from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import xpath_locators, css_locators

driver = webdriver.Safari()
driver.get("https://UserName:Password@qauto2.forstudy.space")

xpath_found = 0
xpath_not_found = 0
css_found = 0
css_not_found = 0

def check_locator(locator, locator_type):
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((locator_type, locator))
        )
        return True
    except TimeoutException:
        return False

try:
    print("Перевірка XPath локаторів:")
    for number, xpath in xpath_locators.items():
        if check_locator(xpath, By.XPATH):
            print(f"XPath локатор {number}: Знайдено")
            xpath_found += 1
        else:
            print(f"XPath локатор {number}: Не знайдено")
            xpath_not_found += 1

    print("\nПеревірка CSS локаторів:")
    for number, css in css_locators.items():
        if check_locator(css, By.CSS_SELECTOR):
            print(f"CSS локатор {number}: Знайдено")
            css_found += 1
        else:
            print(f"CSS локатор {number}: Не знайдено")
            css_not_found += 1

finally:
    driver.quit()

print("\n--- Результати перевірки ---")
print(f"XPath локаторів знайдено: {xpath_found}, не знайдено: {xpath_not_found}")
print(f"CSS локаторів знайдено: {css_found}, не знайдено: {css_not_found}")