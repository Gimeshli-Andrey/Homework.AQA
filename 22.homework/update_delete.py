from models import Student, Course, get_db_connection
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def update_student(db_url, student_id, **kwargs):
    session, _ = get_db_connection(db_url)

    try:
        student = session.get(Student, student_id)

        if student:
            for key, value in kwargs.items():
                setattr(student, key, value)

            session.commit()
            logger.info(f"Дані студента {student_id} оновлено.")
        else:
            logger.warning(f"Студента з ID {student_id} не знайдено.")

    except Exception as e:
        session.rollback()
        logger.error(f"Помилка оновлення: {e}")
    finally:
        session.close()


def delete_student(db_url, student_id):
    session, _ = get_db_connection(db_url)

    try:
        student = session.get(Student, student_id)

        if student:
            session.delete(student)
            session.commit()
            logger.info(f"Студента {student_id} видалено.")
        else:
            logger.warning(f"Студента з ID {student_id} не знайдено.")

    except Exception as e:
        session.rollback()
        logger.error(f"Помилка видалення: {e}")
    finally:
        session.close()


def add_student_to_course(db_url, student_id, course_id):
    session, _ = get_db_connection(db_url)

    try:
        student = session.get(Student, student_id)
        course = session.get(Course, course_id)

        if student and course:
            if course not in student.courses:
                student.courses.append(course)
                session.commit()
                logger.info(f"Студент {student_id} доданий на курс {course_id}")
            else:
                logger.info(f"Студент вже записаний на цей курс")
        else:
            logger.warning("Студент або курс не знайдені")

    except Exception as e:
        session.rollback()
        logger.error(f"Помилка додавання на курс: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    db_url = "postgresql://gimeshli.a:@localhost:5432/bd_name"

    update_student(db_url, 1, age=25, email="new_email@example.com")
    add_student_to_course(db_url, 2, 3)
    delete_student(db_url, 4)