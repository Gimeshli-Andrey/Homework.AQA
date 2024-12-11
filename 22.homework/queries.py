import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Course

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def query_students_for_course(session, course_name):
    course = session.query(Course).filter(Course.name == course_name).first()
    if course:
        students = course.students
        logging.info(f"Студенти на курсі {course_name}: {', '.join([student.name for student in students])}")
        return students
    else:
        logging.error(f"Курс {course_name} не знайдено в базі даних")
        return []

def query_courses_for_student(session, student_name):
    student = session.query(Student).filter(Student.name == student_name).first()
    if student:
        courses = student.courses
        logging.info(f"Курси, на яких зареєстрований студент {student_name}: {', '.join([course.name for course in courses])}")
        return courses
    else:
        logging.error(f"Студент {student_name} не знайдений в базі даних")
        return []

def create_engine_and_session():
    engine = create_engine('sqlite:///university.db', echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

if __name__ == '__main__':
    session = create_engine_and_session()

    query_students_for_course(session, "Course_1")
    query_courses_for_student(session, "Alex")