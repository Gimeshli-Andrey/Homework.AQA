import logging
import os

log_file = '/Users/gimeshli.a/Desktop/Homework.AQA/16.homework/pytest_info.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
)

def initialize_employee(self, name, salary):
    self.name = name
    self.salary = salary
    logging.debug(f'Ініціалізація Employee: {self.name}, Зарплата: {self.salary}')


def initialize_manager(self, name, salary, department):
    initialize_employee(self, name, salary)
    self.department = department
    logging.debug(f'Ініціалізація Manager: Відділ: {self.department}')


def initialize_developer(self, name, salary, programming_language):
    initialize_employee(self, name, salary)
    self.programming_language = programming_language
    logging.debug(f'Ініціалізація Developer: Мова програмування: {self.programming_language}')


class Employee:
    def __init__(self, name, salary):
        initialize_employee(self, name, salary)
        logging.info(f'Створено об\'єкт Employee: {self.name}')

    def __str__(self):
        return f"Employee: {self.name}, Зарплата: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        initialize_manager(self, name, salary, department)
        logging.info(f'Створено об\'єкт Manager: {self.name}, Відділ: {self.department}')

    def __str__(self):
        return f"Manager: {self.name}, Зарплата: {self.salary}, Відділ: {self.department}"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        initialize_developer(self, name, salary, programming_language)
        logging.info(f'Створено об\'єкт Developer: {self.name}, Мова програмування: {self.programming_language}')

    def __str__(self):
        return f"Developer: {self.name}, Зарплата: {self.salary}, Мова програмування: {self.programming_language}"


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        initialize_manager(self, name, salary, department)
        initialize_developer(self, name, salary, programming_language)
        self.team_size = team_size
        logging.info(f'Створено об\'єкт TeamLead: {self.name}, Розмір команди: {self.team_size}')

    def __str__(self):
        return f"TeamLead: {self.name}, Зарплата: {self.salary}, Відділ: {self.department}, " \
               f"Мова програмування: {self.programming_language}, Розмір команди: {self.team_size}"


def test_team_lead_attributes():
    logging.info('Тестування почалося...')

    team_lead = TeamLead("John Doe", 120000, "Engineering", "Python", 5)
    logging.debug(f'Об\'єкт TeamLead створено: {team_lead}')

    assert hasattr(team_lead, 'department'), "TeamLead повинен мати атрибут 'department' з Manager"

    assert hasattr(team_lead,
                   'programming_language'), "TeamLead повинен мати атрибут 'programming_language' з Developer"

    assert hasattr(team_lead, 'team_size'), "TeamLead повинен мати атрибут 'team_size'"

    assert team_lead.name == "John Doe", "Ім'я повинно бути 'John Doe'"
    assert team_lead.salary == 120000, "Зарплата повинна бути 120000"
    assert team_lead.department == "Engineering", "Відділ повинен бути 'Engineering'"
    assert team_lead.programming_language == "Python", "Мова програмування повинна бути 'Python'"
    assert team_lead.team_size == 5, "Розмір команди повинен бути 5"

    logging.info('Тестування успішно завершено.')
    print("Тест пройдено успішно.")


test_team_lead_attributes()

employee = Employee("Alice", 50000)
manager = Manager("Bob", 80000, "HR")
developer = Developer("Charlie", 100000, "Java")
team_lead = TeamLead("David", 120000, "Engineering", "Python", 5)

print(employee)
print(manager)
print(developer)
print(team_lead)

logging.info('Програма завершена.')