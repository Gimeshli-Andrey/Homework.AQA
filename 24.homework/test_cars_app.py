import pytest
import logging
import os
from requests.auth import HTTPBasicAuth
import requests
from datetime import datetime

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_search.log')
print(f"Шлях до лог файлу: {log_file_path}")

try:
    with open(log_file_path, 'a', encoding='utf-8') as f:
        f.write('')
    print(f"Лог файл створено за шляхом: {log_file_path}")
except Exception as e:
    print(f"Не вдалось створити/записати у лог файл: {e}")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

for handler in logger.handlers[:]:
    logger.removeHandler(handler)

file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("Повідомлення для дебагу")
logger.info("Інформаційне повідомлення")
logger.warning("Попереджувальне повідомлення")

test_params = [
    pytest.param(
        'price', '5',
        id='sort_by_price_limit_5'
    ),
    pytest.param(
        'year', '10',
        id='sort_by_year_limit_10'
    ),
    pytest.param(
        'engine_volume', '7',
        id='sort_by_engine_limit_7'
    ),
    pytest.param(
        'brand', '3',
        id='sort_by_brand_limit_3'
    ),
    pytest.param(
        None, '15',
        id='no_sort_limit_15'
    ),
    pytest.param(
        'price', None,
        id='sort_by_price_no_limit'
    ),
    pytest.param(
        None, None,
        id='no_sort_no_limit'
    ),
]

class TestCarsAPI:
    BASE_URL = 'http://127.0.0.1:8080'

    @pytest.fixture(scope='class')
    def auth_session(self):
        logger.info("=" * 50)
        logger.info("Початок процесу аутентифікації")
        session = requests.Session()

        try:
            auth_url = f"{self.BASE_URL}/auth"
            logger.info(f"Спроба аутентифікації: {auth_url}")

            response = session.post(
                auth_url,
                auth=HTTPBasicAuth('test_user', 'test_pass')
            )
            response.raise_for_status()

            token = response.json()['access_token']
            session.headers.update({'Authorization': f'Bearer {token}'})
            logger.info("Аутентифікація успішна. Токен отримано.")

            yield session

        except requests.exceptions.RequestException as e:
            logger.error(f"Помилка при аутентифікації: {str(e)}")
            raise
        finally:
            session.close()
            logger.info("Сесія закрита")
            logger.info("=" * 50)

    @pytest.mark.parametrize("sort_by,limit", test_params)
    def test_search_cars(self, auth_session, sort_by, limit):

        start_time = datetime.now()
        logger.info("-" * 50)
        logger.info(f"Запуск тесту: sort_by={sort_by}, limit={limit}")
        logger.info(f"Час початку: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

        params = {}
        if sort_by:
            params['sort_by'] = sort_by
        if limit:
            params['limit'] = limit

        cars_url = f"{self.BASE_URL}/cars"
        logger.info(f"Відправка GET запиту: {cars_url}")
        logger.info(f"Параметри запиту: {params}")

        response = auth_session.get(cars_url, params=params)

        logger.info(f"Статус код відповіді: {response.status_code}")

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            logger.error(f"Помилка запиту: {e}")

        assert response.status_code == 200, f"Неочікуваний статус код: {response.status_code}"
        cars = response.json()
        assert isinstance(cars, list), "Відповідь має бути списком"

        if cars:
            expected_keys = {'brand', 'year', 'engine_volume', 'price'}
            actual_keys = set(cars[0].keys())
            assert expected_keys == actual_keys, f"Невірна структура даних: {actual_keys}"

        if limit:
            assert len(cars) <= int(limit), f"Перевищено ліміт: {len(cars)} > {limit}"
            logger.info(f"Отримано автомобілів: {len(cars)} з {limit}")
        else:
            logger.info(f"Отримано автомобілів (без ліміту): {len(cars)}")

        if sort_by:
            if sort_by != 'brand':
                values = [car[sort_by] for car in cars]
                assert values == sorted(values), f"Неправильне сортування за {sort_by}"
                logger.info(f"Сортування за {sort_by} коректне")
                logger.info(f"Значення {sort_by}: {values[:5]}...")
            else:
                values = [car[sort_by].lower() for car in cars]
                assert values == sorted(values), "Неправильне сортування за brand"
                logger.info("Сортування за brand коректне")
                logger.info(f"Бренди: {values[:5]}...")

        end_time = datetime.now()
        logger.info(f"Час завершення: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"Тривалість тесту: {end_time - start_time}")

        logger.info("Тест успішно завершений")
        logger.info("-" * 50)