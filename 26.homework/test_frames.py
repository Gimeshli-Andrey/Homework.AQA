import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from logger_setup import setup_logger

logger = setup_logger()


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')

    driver = webdriver.Chrome(options=chrome_options)

    logger.info("Chrome driver initialized")

    yield driver

    driver.quit()
    logger.info("Chrome driver closed")


def handle_frame(driver, frame_id, secret_text, expected_alert_text):
    try:
        wait = WebDriverWait(driver, 10)

        frame = wait.until(EC.presence_of_element_located((By.ID, frame_id)))
        driver.switch_to.frame(frame)
        logger.info(f"Switched to frame: {frame_id}")

        input_field = wait.until(EC.presence_of_element_located((By.ID, f"input{frame_id[-1]}")))
        logger.info(f"Input field found in frame {frame_id}")

        verify_button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
        logger.info(f"Verify button found in frame {frame_id}")

        input_field.clear()
        input_field.send_keys(secret_text)
        logger.info(f"Entered secret text into frame: {frame_id}")

        verify_button.click()
        logger.info(f"Clicked 'Verify' button in frame: {frame_id}")

        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        logger.info(f"Alert received in frame {frame_id}: {alert_text}")

        assert alert_text == expected_alert_text, f"Expected alert text '{expected_alert_text}', but got '{alert_text}'"

        alert.accept()
        logger.info(f"Alert accepted in frame {frame_id}")

        driver.switch_to.default_content()
        logger.info(f"Switched back to default content from frame: {frame_id}")

        return alert_text

    except Exception as e:
        logger.error(f"Error occurred while handling frame {frame_id}: {str(e)}")
        driver.switch_to.default_content()
        raise e


def test_frames(driver):
    try:
        driver.get("http://localhost:8000/dz.html")
        logger.info("Navigated to http://localhost:8000/dz.html")

        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
        logger.info("Page loaded successfully")

        try:
            driver.find_element(By.ID, "frame1")
            logger.info("Frame 1 is present on the page")
        except Exception:
            logger.error("Frame 1 not found on the page")
            raise AssertionError("Frame 1 not found on the page")

        try:
            driver.find_element(By.ID, "frame2")
            logger.info("Frame 2 is present on the page")
        except Exception:
            logger.error("Frame 2 not found on the page")
            raise AssertionError("Frame 2 not found on the page")

        expected_alert_text = "Верифікація пройшла успішно!"

        # Frame 1
        logger.info("Processing frame frame1")
        frame1_alert = handle_frame(driver, "frame1", "Frame1_Secret", expected_alert_text)
        logger.info("Verification passed for frame1")

        # Frame 2
        logger.info("Processing frame frame2")
        frame2_alert = handle_frame(driver, "frame2", "Frame2_Secret", expected_alert_text)
        logger.info("Verification passed for frame2")

        assert frame1_alert == expected_alert_text, "Frame 1 verification failed"
        assert frame2_alert == expected_alert_text, "Frame 2 verification failed"

        logger.info("Both frame verifications passed")

    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        driver.save_screenshot('error_screenshot.png')
        logger.info("Screenshot saved as error_screenshot.png")
        raise e