import pandas as pd
import logging
import os

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'homework_log.log')


def setup_logger():
    logger = logging.getLogger('remove_duplicates_logger')
    handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def remove_duplicates(input_file1, input_file2, output_file):
    logger = setup_logger()
    logger.info("Початок виконання скрипта")

    try:
        df1 = pd.read_csv(input_file1)
        logger.info(f'Успішно прочитано файл: {input_file1}')

        df2 = pd.read_csv(input_file2)
        logger.info(f'Успішно прочитано файл: {input_file2}')

        combined_df = pd.concat([df1, df2]).drop_duplicates()
        logger.info('Дублікати успішно видалені.')

        combined_df.to_csv(output_file, index=False)
        logger.info(f'Результат успішно записано у файл: {output_file}')

    except FileNotFoundError as e:
        logger.error(f'Файл не знайдено: {e}')
    except pd.errors.EmptyDataError:
        logger.error('Один із файлів порожній.')
    except Exception as e:
        logger.error(f'Сталася помилка: {e}')

    logger.info("Завершення виконання скрипта")


if __name__ == '__main__':
    input_file1 = '/Users/gimeshli.a/Desktop/Homework.AQA/13.homework/work_with_csv/r-m-c.csv'
    input_file2 = '/Users/gimeshli.a/Desktop/Homework.AQA/13.homework/work_with_csv/rmc.csv'
    output_file = '/Users/gimeshli.a/Desktop/Homework.AQA/13.homework/result_gimeshli.csv'

    remove_duplicates(input_file1, input_file2, output_file)