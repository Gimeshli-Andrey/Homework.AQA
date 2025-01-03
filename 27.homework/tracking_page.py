from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from logger import setup_logger

class TrackingPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"
        self.logger = setup_logger()

    def open(self):
        self.logger.info("Відкриття сторінки трекінгу...")
        self.driver.get(self.url)

    def enter_tracking_number(self, tracking_number):
        self.logger.info(f"Введення номера накладної: {tracking_number}")
        input_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        input_field.clear()
        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.RETURN)

    def get_status(self):
        try:

            status_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
            )
            self.logger.info(f"Статус посилки: {status_element.text}")
            return status_element.text
        except Exception as e:
            self.logger.error(f"Помилка при отриманні статусу: {e}")
            return "Статус не знайдено"