import random
import time
from flask import Flask, request, jsonify
from src.db_base import SQLiteActions
import os

app = Flask(__name__)
SECRET_KEY = 'token_secret_key'

def ensure_database_exists():
    db_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bd_log')
    os.makedirs(db_dir, exist_ok=True)
    db_path_1 = os.path.join(db_dir, 'test_database.db')
    db_path_2 = os.path.join(db_dir, 'test.db')

    open(db_path_1, 'a').close()
    open(db_path_2, 'a').close()

ensure_database_exists()

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bd_log', 'test_database.db')

db = SQLiteActions(db_path)

@app.route('/students/', methods=['GET'])
def get_students():
    data = db.get_students()
    return jsonify(data), 200

@app.route('/auth/', methods=['POST'])
def get_token():
    is_user_data_correct_user = True
    user_data = request.get_json()

    if user_data.get('name') != 'test':
        is_user_data_correct_user = False

    if user_data.get('password') != 'test':
        is_user_data_correct_user = False

    if not is_user_data_correct_user:
        return jsonify("incorrect user name or password"), 403

    return SECRET_KEY, 200

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id: str):
    if not student_id.isnumeric():
        return jsonify({'error': 'student_id should be int'}), 400

    data = db.get_student(student_id)
    if not data:
        return jsonify({'error': 'Student with this id does not exist'}), 404

    return jsonify(data), 200

@app.route('/students/', methods=['POST'])
def create_students():
    auth_res = check_auth(request.headers)
    if auth_res is not None:
        return jsonify(auth_res[0]), auth_res[1]

    request_data = request.get_json()
    time.sleep(random.random() + 1.5)  # sleep 1.5-2.5 sec
    error_msgs = []
    name = request_data.get('name')
    score = request_data.get('score', 0)

    if not name:
        error_msgs.append("You have to input name")
    if not 0 < score <= 100:
        error_msgs.append("Score must be between 1 and 100")

    if error_msgs:
        return jsonify(error_msgs), 400

    student = db.add_student(name=name, score=score)
    return jsonify(student), 201

@app.route('/students/<student_id>', methods=['PUT'])
def update_students(student_id):
    auth_res = check_auth(request.headers)
    if auth_res is not None:
        return jsonify(auth_res[0]), auth_res[1]

    request_data = request.get_json()
    name = request_data.get('name')
    score = request_data.get('score')

    student = db.get_student(student_id)

    if not name and not score:
        return jsonify({'message': 'You have to put name and/or score of the student'}), 400

    name = name if name is not None else student['name']
    score = score if score is not None else student['score']
    student = db.update_student(student_id=student_id, name=name, score=score)
    return jsonify(student), 200

@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    auth_res = check_auth(request.headers)
    if auth_res is not None:
        return jsonify(auth_res[0]), auth_res[1]

    db.delete_student(student_id)
    return jsonify({'message': f'Student {student_id} deleted'}), 204

def check_auth(headers):
    if headers.get('token') is None:
        return "You are not authorized", 401

    if headers.get('token') != SECRET_KEY:
        return "Token is incorrect", 403

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)