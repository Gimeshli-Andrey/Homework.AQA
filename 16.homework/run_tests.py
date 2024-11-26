import subprocess
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def run_python_script(script_name):
    logging.info(f"Запуск {script_name}...")
    try:
        result = subprocess.run(["python", script_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Завершено: {script_name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Помилка при виконанні {script_name}: {e}")
        logging.error(f"Виведення: {e.stdout.decode()}")
        logging.error(f"Помилки: {e.stderr.decode()}")
        return False
    return True

def run_pytest_tests(test_file):
    logging.info(f"Запуск тестів для {test_file} за допомогою pytest...")
    try:
        with open("pytest_info.log", "a") as log_file:
            result = subprocess.run(
                ["pytest", test_file, "--maxfail=5", "--disable-warnings", "--capture=no"],
                stdout=log_file, stderr=log_file, check=True
            )
        logging.info(f"Тести для {test_file} завершені")
    except subprocess.CalledProcessError as e:
        logging.error(f"Помилка при виконанні тестів для {test_file}")
        return False
    return True

if __name__ == "__main__":
    if run_python_script("task_16_1.py") and run_python_script("task_16_2.py"):
        run_pytest_tests("test_task_16_1.py")
        run_pytest_tests("test_task_16_2.py")