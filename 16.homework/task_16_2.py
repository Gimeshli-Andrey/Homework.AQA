import logging
import os
from abc import ABC, abstractmethod
from math import pi

file_name = os.path.basename(__file__)

logging.basicConfig(filename='/Users/gimeshli.a/Desktop/Homework.AQA/16.homework/pytest_info.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(filename)s - %(message)s')

logging.info("Початок виконання програми.")


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return pi * self.__radius ** 2

    def perimeter(self):
        return 2 * pi * self.__radius


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")
        self.__a = a
        self.__b = b
        self.__c = c

    def get_sides(self):
        return self.__a, self.__b, self.__c

    def area(self):
        s = (self.__a + self.__b + self.__c) / 2
        return (s * (s - self.__a) * (s - self.__b) * (s - self.__c)) ** 0.5

    def perimeter(self):
        return self.__a + self.__b + self.__c


shapes = [Rectangle(10, 5), Circle(7), Triangle(3, 4, 5)]

for shape in shapes:
    logging.info(f"Початок обчислень для {shape.__class__.__name__}.")

    if isinstance(shape, Rectangle):
        logging.info(f"Прямокутник: ширина={shape.get_width()}, висота={shape.get_height()}, "
                     f"Площа = {shape.area()}, Периметр = {shape.perimeter()}")
    elif isinstance(shape, Circle):
        logging.info(f"Коло: радіус={shape.get_radius()}, Площа = {shape.area()}, Периметр = {shape.perimeter()}")
    elif isinstance(shape, Triangle):
        logging.info(f"Трикутник: сторони={shape.get_sides()}, Площа = {shape.area()}, Периметр = {shape.perimeter()}")

    logging.info(f"Завершення обчислень для {shape.__class__.__name__}.")

logging.info("Завершення виконання програми.")