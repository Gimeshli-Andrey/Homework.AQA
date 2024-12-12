import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Course

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def update_student_age(session, student_name, new_age):
    student = session.query(Student).filter(Student.name == student_name).first()
    if student:
        student.age = new_age
        session.commit()
        logging.info(f"Вік студента {student_name} оновлено на {new_age}")
    else:
        logging.error(f"Студент {student_name} не знайдений в базі даних")

def delete_student(session, student_name):
    student = session.query(Student).filter(Student.name == student_name).first()
    if student:
        session.delete(student)
        session.commit()
        logging.info(f"Студент {student_name} видалений з бази даних")
    else:
        logging.error(f"Студент {student_name} не знайдений в базі даних")

def create_engine_and_session():
    engine = create_engine('sqlite:///university.db', echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

if __name__ == '__main__':
    session = create_engine_and_session()

    update_student_age(session, "Alex", 24)
    delete_student(session, "Kate")
