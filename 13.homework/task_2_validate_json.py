import os
import json
import logging

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'homework_log.log')


def setup_logger():
    logger = logging.getLogger('validate_json_logger')
    handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def validate_json_files(directory):
    logger = setup_logger()
    logger.info("Початок виконання скрипта")

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r') as f:
                    json.load(f)
                logger.info(f"{filename} - валідний JSON.")
            except json.JSONDecodeError:
                logger.error(f"{filename} - невалідний JSON.")
            except Exception as e:
                logger.error(f"Помилка при обробці файлу {filename}: {e}")

    logger.info("Завершення виконання скрипта")

if __name__ == '__main__':
    json_directory = '/Users/gimeshli.a/Desktop/Homework.AQA/13.homework/work_with_json'
    validate_json_files(json_directory)