import logging
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course, StudentCourse

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_courses_and_students(session):
    try:
        courses = [Course(name=f"Курс_{i}") for i in range(1, 6)]
        session.add_all(courses)
        session.commit()
        logging.info("Курси створені та збережені у базі даних.")

        students_names = [
            "Олексій", "Катерина", "Ольга", "Марія", "Єва", "Джеймс", "Мія", "Давид", "Хлоя", "Ліам",
            "Софія", "Джек", "Ізабелла", "Айден", "Емілія", "Лукас", "Мейсон", "Амелія", "Ітан", "Зоя"
        ]
        students = [Student(name=name, age=random.randint(18, 25)) for name in students_names]
        session.add_all(students)
        session.commit()
        logging.info("Студенти створені та збережені у базі даних.")

        for student in students:
            random_courses = random.sample(courses, random.randint(1, 3))
            for course in random_courses:
                student_course = StudentCourse(student_id=student.id, course_id=course.id)
                session.add(student_course)
        session.commit()
        logging.info("Студенти зареєстровані на курси.")

    except Exception as e:
        session.rollback()
        logging.error(f"Помилка під час створення даних: {e}")
        raise

def create_engine_and_session():
    try:
        engine = create_engine('sqlite:///university.db', echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session()
    except Exception as e:
        logging.error(f"Помилка під час налаштування бази даних: {e}")
        raise

if __name__ == '__main__':
    session = create_engine_and_session()
    create_courses_and_students(session)