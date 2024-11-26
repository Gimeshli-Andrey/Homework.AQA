# --- Завдання 1: Генератори ---

# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# --- Завдання 2: Ітератори ---

# Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration


# --- Завдання 3: Декоратори ---

# Напишіть декоратор, який логує аргументи та результати викликаної функції.
def log_args_and_results(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None
    return wrapper


# --- Приклад використання ---

# Генератори
print("Генератор парних чисел до 10:")
for num in even_numbers(10):
    print(num)

print("\nГенератор послідовності Фібоначчі до 20:")
for num in fibonacci(20):
    print(num)


# Ітератори
print("\nІтератор для зворотного виведення елементів списку:")
my_list = [1, 2, 3, 4, 5]
reverse_iter = ReverseIterator(my_list)
for item in reverse_iter:
    print(item)

print("\nІтератор для парних чисел в діапазоні до 10:")
even_iter = EvenIterator(10)
for num in even_iter:
    print(num)


# Декоратори
@log_args_and_results
def add(a, b):
    return a + b

print("\nВикористання декоратора для логування аргументів і результату:")
add(2, 3)

@handle_exceptions
def divide(a, b):
    return a / b

print("\nВикористання декоратора для обробки винятків:")
print(divide(10, 0))
print(divide(10, 2))