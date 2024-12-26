from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Safari()
driver.get("https://UserName:Password@qauto2.forstudy.space")

# XPath
xpath_locators = {
    # Форма входу та реєстрації
    1: "//input[@id='signinEmail']",  # Поле email при вході
    2: "//input[contains(@id, 'password')]",  # Поле пароля
    3: "//button[text()='Sign in']",  # Кнопка входу
    4: "//button[contains(text(), 'Registration')]",  # Кнопка реєстрації
    5: "//div[contains(@class, 'form-signin')]//input[@type='email']",  # Поле email у формі

    # Навігація та хедер
    6: "//nav//a[text()='Home']",  # Посилання на головну сторінку
    7: "//div[contains(@class, 'header')]//button[contains(@class, 'profile-button')]",  # Кнопка профілю
    8: "//a[contains(@class, 'nav-link') and contains(text(), 'Garage')]",  # Посилання на гараж
    9: "//div[@class='header']//img[@alt='avatar']",  # Аватар користувача
    10: "//button[text()='Log out']",  # Кнопка виходу

    # Гараж
    11: "//button[contains(@class, 'btn-primary') and text()='Add car']",  # Кнопка додавання машини
    12: "//select[contains(@id, 'brands')]//option[text()='BMW']",  # Опція BMW у селекті брендів
    13: "//input[@placeholder='Enter mileage']",  # Поле пробігу
    14: "(//div[contains(@class, 'car-item')])[last()]",  # Остання додана машина
    15: "//div[@class='car-list']//div[contains(@class, 'car-item')]",  # Список машин

    # Профіль
    16: "//div[contains(@class, 'profile-form')]//input[@id='name']",  # Поле імені у профілі
    17: "//button[contains(@class, 'edit-profile') and text()='Edit profile']",  # Кнопка редагування профілю
    18: "//div[contains(@class, 'profile-details')]//span[text()='Email']/following-sibling::span",  # Email у профілі
    19: "//form[@id='profile-form']//button[@type='submit']",  # Кнопка збереження профілю
    20: "//div[contains(@class, 'profile-stats')]//div[contains(@class, 'stats-item')]",  # Статистика профілю

    # Витрати та інші елементи
    21: "//table[@id='expenses-table']//tbody//tr[1]//td[1]",  # Перша клітинка таблиці витрат
    22: "//div[contains(@class, 'alert')]//button[@class='close']",  # Кнопка закриття алерта
    23: "//div[contains(@class, 'settings')]//label[contains(text(), 'Currency')]",  # Мітка валюти
    24: "//button[contains(@class, 'btn-danger') and text()='Remove']",  # Кнопка видалення
    25: "//div[contains(@class, 'pagination')]//button[contains(@class, 'active')]"  # Активна сторінка пагінації
}

# CSS
css_locators = {
    1: "#signinEmail",  # Поле email
    2: "#signinPassword",  # Поле пароля
    3: "button.btn-primary",  # Основна кнопка
    4: ".form-signin input[type='email']",  # Поле email у формі входу
    5: ".nav-link.active",  # Активне посилання навігації

    6: ".header .profile-button",  # Кнопка профілю в хедері
    7: "nav .navbar-brand",  # Логотип
    8: ".garage-empty-title",  # Заголовок пустого гаража
    9: ".car-item img.car-image",  # Зображення машини
    10: ".profile-nav .nav-item",  # Елемент навігації профілю

    11: "form.add-car-form select#brand",  # Селект бренду
    12: ".car-list .car-item:first-child",  # Перша машина у списку
    13: "input[type='number'][name='mileage']",  # Поле пробігу
    14: ".expenses-table tbody tr:last-child",  # Останній рядок витрат
    15: ".settings-form input[type='checkbox']",  # Чекбокс у налаштуваннях

    16: ".profile-form #name",  # Поле імені
    17: ".alert.alert-success",  # Повідомлення про успіх
    18: ".modal-dialog .modal-content",  # Вміст модального вікна
    19: "button.btn-outline-dark",  # Кнопка з темним контуром
    20: ".pagination .page-item.active",  # Активна сторінка

    21: "table.expenses-table > thead > tr",  # Заголовок таблиці витрат
    22: ".dropdown-menu.show",  # Відкрите випадаюче меню
    23: "form.edit-profile-form",  # Форма редагування профілю
    24: ".stats-block .stats-item",  # Елемент статистики
    25: ".footer .copyright"  # Копірайт у футері
}

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
        result = check_locator(xpath, By.XPATH)
        print(f"XPath локатор {number}: {'Знайдено' if result else 'Не знайдено'}")

    print("\nПеревірка CSS локаторів:")
    for number, css in css_locators.items():
        result = check_locator(css, By.CSS_SELECTOR)
        print(f"CSS локатор {number}: {'Знайдено' if result else 'Не знайдено'}")
finally:
    driver.quit()