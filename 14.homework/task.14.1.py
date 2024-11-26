import logging

logging.basicConfig(
    filename='pytest_info.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade
        logging.info(f"Створено студента: Ім'я: {self.first_name}, Прізвище: {self.last_name}, Вік: {self.age}, Середній бал: {self.average_grade}")

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade
        logging.info(f"Середній бал змінено: Новий середній бал: {self.average_grade}")

    def display_info(self):
        print(f"Ім'я: {self.first_name}")
        print(f"Прізвище: {self.last_name}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.average_grade}")

if __name__ == "__main__":
    logging.info("Початок виконання програми")

    student = Student("Андрій", "Гімешлі", 29, 4.5)

    student.display_info()

    student.change_average_grade(4.8)

    print("\nПісля зміни середнього балу:")
    student.display_info()

    logging.info("Завершення виконання програми")
