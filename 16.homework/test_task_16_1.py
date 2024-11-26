import pytest
import logging
from task_16_1 import Employee, Manager, Developer, TeamLead

log_file = '/Users/gimeshli.a/Desktop/Homework.AQA/16.homework/pytest_info.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
)


def test_employee_creation():
    employee = Employee("Alice", 50000)
    logging.info(f'Тест створення Employee: {employee}')

    assert isinstance(employee, Employee), "Об'єкт не є інстанцією Employee"
    assert employee.name == "Alice", "Ім'я співробітника повинно бути 'Alice'"
    assert employee.salary == 50000, "Зарплата співробітника повинна бути 50000"
    logging.info("Тест Employee пройшов успішно.")


def test_manager_creation():
    manager = Manager("Bob", 80000, "HR")
    logging.info(f'Тест створення Manager: {manager}')

    assert isinstance(manager, Manager), "Об'єкт не є інстанцією Manager"
    assert manager.name == "Bob", "Ім'я менеджера повинно бути 'Bob'"
    assert manager.salary == 80000, "Зарплата менеджера повинна бути 80000"
    assert manager.department == "HR", "Відділ менеджера повинен бути 'HR'"
    logging.info("Тест Manager пройшов успішно.")


def test_team_lead_creation():
    team_lead = TeamLead("David", 120000, "Engineering", "Python", 5)
    logging.info(f'Тест створення TeamLead: {team_lead}')

    assert isinstance(team_lead, TeamLead), "Об'єкт не є інстанцією TeamLead"
    assert team_lead.name == "David", "Ім'я TeamLead повинно бути 'David'"
    assert team_lead.salary == 120000, "Зарплата TeamLead повинна бути 120000"
    assert team_lead.department == "Engineering", "Відділ TeamLead повинен бути 'Engineering'"
    assert team_lead.programming_language == "Python", "Мова програмування TeamLead повинна бути 'Python'"
    assert team_lead.team_size == 5, "Розмір команди TeamLead повинен бути 5"
    logging.info("Тест TeamLead пройшов успішно.")


def test_employee_creation_missing_name():
    with pytest.raises(AssertionError):
        employee = Employee("", 50000)
        assert employee.name != "", "Ім'я не повинно бути порожнім"


def test_manager_creation_invalid_department():
    with pytest.raises(AssertionError):
        manager = Manager("Bob", 80000, "Unknown")
        assert manager.department == "HR", "Відділ повинен бути 'HR'"


def test_team_lead_creation_invalid_team_size():
    with pytest.raises(AssertionError):
        team_lead = TeamLead("David", 120000, "Engineering", "Python", -1)
        assert team_lead.team_size > 0, "Розмір команди повинен бути позитивним числом"