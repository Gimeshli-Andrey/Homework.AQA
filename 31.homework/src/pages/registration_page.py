import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegistrationPage(BasePage):
    FIRSTNAME_INPUT = (By.XPATH, "//input[@name='firstname']")
    LASTNAME_INPUT = (By.XPATH, "//input[@name='lastname']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PHONE_INPUT = (By.XPATH, "//input[@name='phone']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@name='confirm_password']")
    REGISTER_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Вхід')]")

    @allure.step("Fill registration form")
    def fill_registration_form(self, user_data):
        self.input_text(self.FIRSTNAME_INPUT, user_data['firstname'])
        self.input_text(self.LASTNAME_INPUT, user_data['lastname'])
        self.input_text(self.EMAIL_INPUT, user_data['email'])
        self.input_text(self.PHONE_INPUT, user_data['phone'])
        self.input_text(self.PASSWORD_INPUT, user_data['password'])
        self.input_text(self.CONFIRM_PASSWORD_INPUT, user_data['password'])

    @allure.step("Click register button")
    def click_register(self):
        self.click_element(self.REGISTER_BUTTON)

    @allure.step("Navigate to login page")
    def go_to_login(self):
        self.click_element(self.LOGIN_LINK)