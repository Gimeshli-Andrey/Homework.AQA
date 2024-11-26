import csv
import random
import os

file_path = '/Users/gimeshli.a/Desktop/Homework.AQA/17.homework/randominfo-master/randominfo/data.csv'
image_folder = '/Users/gimeshli.a/Desktop/Homework.AQA/17.homework/randominfo-master/randominfo/images/people'

with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames
    print(f"Заголовки столбцов: {headers}")
    rows = list(reader)

images = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

if len(images) < len(rows):
    print("Внимание: Количество изображений меньше, чем записей в CSV файле!")

random_person = random.choice(rows)
random_image = random.choice(images)

print("=" * 80)
print(f"{'First Name':<15}: {random_person.get('firstname', 'N/A')}")
print(f"{'Last Name':<15}: {random_person.get('lastname', 'N/A')}")
print(f"{'Gender':<15}: {random_person.get('gender', 'N/A')}")
print(f"{'Hobbies':<15}: {random_person.get('hobbies', 'N/A')}")
print(f"{'Street Address':<15}: {random_person.get('street address', 'N/A')}")
print(f"{'Landmark':<15}: {random_person.get('landmark', 'N/A')}")
print(f"{'Area':<15}: {random_person.get('area', 'N/A')}")
print(f"{'City':<15}: {random_person.get('city', 'N/A')}")
print(f"{'State':<15}: {random_person.get('state', 'N/A')}")
print(f"{'Pincode':<15}: {random_person.get('pincode', 'N/A')}")
print(f"{'Image':<15}: {os.path.join(image_folder, random_image)}")
print("=" * 80)