import xml.etree.ElementTree as ET
import logging
import os

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'homework_log.log')

def setup_logger():
    logger = logging.getLogger('find_in_xml_logger')
    handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logger()

def find_incoming_by_group_number(xml_file, group_number):
    logger.info("Початок виконання скрипта")

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number').text
            if number == str(group_number):
                incoming_value = group.find('timingExbytes/incoming').text
                logger.info(f'Incoming value for group {group_number}: {incoming_value}')
                logger.info("Завершення виконання скрипта")
                return incoming_value

        logger.info(f'Group number {group_number} not found.')
    except FileNotFoundError:
        logger.error(f'File {xml_file} not found.')
    except Exception as e:
        logger.error(f'An error occurred: {e}')

    logger.info("Завершення виконання скрипта")

if __name__ == '__main__':
    group_number_to_search = 2
    xml_file = '/Users/gimeshli.a/Desktop/Homework.AQA/13.homework/work_with_xml/groups.xml'

    incoming_value = find_incoming_by_group_number(xml_file, group_number_to_search)

    if incoming_value:
        print(f'Incoming value for group {group_number_to_search}: {incoming_value}')
    else:
        print(f'Group number {group_number_to_search} not found or has no incoming value.')