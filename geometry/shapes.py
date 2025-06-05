# Основные классы фигур
from math import pi, sqrt


class Shape:
    def get_area(self):
        raise NotImplementedError("Subclasses should implement this!")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self._validate_triangle()

    def _validate_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        if not all(side > 0 for side in sides):
            raise ValueError("All sides should be positive")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Triangle inequality violated")

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9