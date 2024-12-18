import random
from sqlalchemy import text
from models import Base, Student, Course, get_db_connection, logger


def create_tables(engine):
    try:
        Base.metadata.drop_all(engine)

        Base.metadata.create_all(engine)
        logger.info("Таблиці успішно створені")
    except Exception as e:
        logger.error(f"Помилка створення таблиць: {e}")


def create_test_data(db_url):
    session, engine = get_db_connection(db_url)

    create_tables(engine)

    courses_data = [
        {"title": "Програмування", "description": "Основи розробки ПЗ"},
        {"title": "Бази Даних", "description": "Вивчення SQL та ORM"},
        {"title": "Комп'ютерні мережі", "description": "Архітектура мереж"},
        {"title": "Штучний Інтелект", "description": "Машинне навчання"},
        {"title": "Кібербезпека", "description": "Захист інформаційних систем"}
    ]

    try:
        courses = [Course(**data) for data in courses_data]
        session.add_all(courses)
        session.commit()

        names = [
            "Іван Петров", "Марія Коваленко", "Андрій Сидоренко",
            "Олена Мельник", "Тетяна Шевченко", "Максим Кузнецов",
            "Наталія Гончарова", "Роман Ткаченко", "Світлана Мартинова",
            "Дмитро Зінченко", "Юлія Поліщук", "Олег Бондаренко",
            "Віктор Кравченко", "Ірина Литвин", "Богдан Мороз",
            "Катерина Данилюк", "Артем Панасюк", "Валентина Степанова",
            "Микола Токар", "Ганна Гриценко"
        ]

        students = []
        for i, name in enumerate(names, 1):
            student = Student(
                name=name,
                age=random.randint(18, 30),
                email=f"student{i}@example.com"
            )

            student_courses = random.sample(courses, random.randint(1, 3))
            student.courses.extend(student_courses)

            students.append(student)

        session.add_all(students)
        session.commit()

        logger.info("Тестові дані успішно створено!")

    except Exception as e:
        session.rollback()
        logger.error(f"Помилка при створенні даних: {e}")

    finally:
        session.close()


if __name__ == "__main__":
    db_url = "postgresql://gimeshli.a:@localhost:5432/bd_name"
    create_test_data(db_url)