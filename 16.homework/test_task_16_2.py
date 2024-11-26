import pytest
import math
from task_16_2 import Rectangle, Circle

def test_rectangle_area_positive():
    rectangle = Rectangle(10, 5)
    assert rectangle.area() == 50, f"Очікувалась площа прямокутника 50, але отримано {rectangle.area()}"

def test_circle_area_positive():
    circle = Circle(7)
    expected_area = math.pi * 7 ** 2
    assert circle.area() == pytest.approx(expected_area, rel=1e-2), \
        f"Очікувалась площа кола {expected_area}, але отримано {circle.area()}"

def test_rectangle_perimeter_positive():
    rectangle = Rectangle(10, 5)
    expected_perimeter = 2 * (10 + 5)
    assert rectangle.perimeter() == expected_perimeter, f"Очікувався периметр {expected_perimeter}, але отримано {rectangle.perimeter()}"


def test_rectangle_invalid_dimensions_negative():
    with pytest.raises(ValueError):
        Rectangle(-10, 5)
    with pytest.raises(ValueError):
        Rectangle(10, -5)

def test_circle_invalid_radius_negative():
    with pytest.raises(ValueError):
        Circle(-5)  # Від'ємний радіус

def test_zero_dimensions_negative():
    with pytest.raises(ValueError):
        Rectangle(0, 5)
    with pytest.raises(ValueError):
        Circle(0)