# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f"{number}x{multiplier}={result}")

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(a, b):
    return a + b

result1 = sum_two_numbers(5, 7)
print(f"Suma 5 + 7 = : {result1}")

result2 = sum_two_numbers(10, 15)
print(f"Suma 10 + 15 = : {result2}")


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_of_list(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
print(average_of_list([1, 2, 3, 4, 5]))  # Виведе 3.0

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]
input_string = "Написати функцію"
reversed_string = reverse_string(input_string)
print(f"Зворотний рядок: {reversed_string}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    if not words:
        return ""
    return max(words, key=len)
print(longest_word(["apple", "banana", "cherry", "strawberry"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    return index if index != -1 else -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # Виведе 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # Виведе -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
def is_even(number):
    """
    Параметри: number (int): Число, яке перевіряється.
    Повертає: bool: True, якщо число парне, і False, якщо непарне.
    """
    return number % 2 == 0

print(is_even(10))  # Виведе True
print(is_even(7))  # Виведе False

# task 8
def find_min(numbers):
    """
    Параметри: numbers (list): Список чисел.
    Повертає: int: Мінімальне число у списку.
    """
    return min(numbers)

print(find_min([4, 1, 9, -3, 6]))  # Виведе -3

# task 9
def reverse_string(s):
    """
    Параметри: s (str): Вхідний рядок.
    Повертає: str: Рядок у зворотному порядку.
    """
    return s[::-1]

print(reverse_string("Python"))  # Виведе 'nohtyP'

# task 10
def calculate_average(numbers):
    """
    Параметри: numbers (list): Список чисел.
    Повертає: float: Середнє арифметичне чисел.
    """
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30, 40]))  # Виведе 25.0