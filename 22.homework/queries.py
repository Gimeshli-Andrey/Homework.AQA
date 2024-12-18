from sqlalchemy import select
from models import Student, Course, get_db_connection, logger


def get_students_by_course(db_url, course_title):
    session, _ = get_db_connection(db_url)

    try:
        course = session.query(Course).filter(Course.title == course_title).first()

        if course:
            logger.info(f"Студенти курсу '{course_title}':")
            for student in course.students:
                logger.info(f"- {student.name}")
            return course.students
        else:
            logger.warning(f"Курс '{course_title}' не знайдено.")
            return []

    except Exception as e:
        logger.error(f"Помилка при отриманні даних: {e}")
        return []
    finally:
        session.close()


def get_courses_by_student(db_url, student_name):
    session, _ = get_db_connection(db_url)

    try:
        student = session.query(Student).filter(Student.name == student_name).first()

        if student:
            logger.info(f"Курси студента {student_name}:")
            for course in student.courses:
                logger.info(f"- {course.title}")
            return student.courses
        else:
            logger.warning(f"Студента '{student_name}' не знайдено.")
            return []

    except Exception as e:
        logger.error(f"Помилка при отриманні даних: {e}")
        return []
    finally:
        session.close()


if __name__ == "__main__":
    db_url = "postgresql://gimeshli.a:@localhost:5432/bd_name"

    get_students_by_course(db_url, "Бази Даних")
    get_courses_by_student(db_url, "Іван Петров")