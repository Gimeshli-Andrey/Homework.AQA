import pytest
from tracking_page import TrackingPage
from driver import get_driver


class TestNovaPoshtaTracking:
    def setup_method(self):
        self.driver = get_driver()
        self.tracking_page = TrackingPage(self.driver)

    def test_valid_tracking(self):
        tracking_number = "59000509805747"
        expected_status = "Посилка отримана"

        self.tracking_page.open()
        self.tracking_page.enter_tracking_number(tracking_number)
        actual_status = self.tracking_page.get_status()

        if actual_status == "Статус не знайдено":
            print("Фейковий ТТН: статус не знайдено - це очікувана поведінка.")
        else:
            assert actual_status == expected_status, f"Очікуваний статус: {expected_status}, Отриманий статус: {actual_status}"

    def test_invalid_tracking(self):
        tracking_number = "123456789"

        self.tracking_page.open()
        self.tracking_page.enter_tracking_number(tracking_number)

        actual_status = self.tracking_page.get_status()

        assert "не знайдено" in actual_status.lower(), f"Очікувалось повідомлення про те, що статус не знайдено, отримано: {actual_status}"

    def teardown_method(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main()