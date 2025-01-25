import pytest
import allure
from src.app import app
from src.db_base import SQLiteActions
import os


@pytest.fixture
def client():
    app.config['TESTING'] = True
    db_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bd_log')
    app.config['DATABASE'] = os.path.join(db_dir, 'test.db')

    os.makedirs(db_dir, exist_ok=True)
    db_path = os.path.join(db_dir, 'test.db')

    open(db_path, 'a').close()

    with app.test_client() as client:
        with app.app_context():
            db = SQLiteActions(db_path, add_random_students=False)
            yield client


@allure.feature('Student Management')
@allure.story('Get Students')
def test_get_students(client):
    response = client.get('/students/')
    assert response.status_code == 200


@allure.feature('Student Management')
@allure.story('Create Student')
def test_create_student(client):
    response = client.post('/students/', json={'name': 'John Doe', 'score': 85}, headers={'token': 'token_secret_key'})
    assert response.status_code == 201
    assert 'id' in response.get_json()


@allure.feature('Student Management')
@allure.story('Get Student')
def test_get_student(client):
    response = client.post('/students/', json={'name': 'John Doe', 'score': 85}, headers={'token': 'token_secret_key'})
    student_id = response.get_json()['id']
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200


@allure.feature('Student Management')
@allure.story('Get Student Not Found')
def test_get_student_not_found(client):
    response = client.get('/students/999')
    assert response.status_code == 404


@allure.feature('Authentication')
@allure.story('Incorrect Auth')
def test_auth_incorrect(client):
    response = client.post('/auth/', json={'name': 'wrong', 'password': 'wrong'})
    assert response.status_code == 403