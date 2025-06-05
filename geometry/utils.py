# Полиморфный интерфейс и поддержка новых фигур
from .shapes import Shape
def calculate_area(shape: Shape) -> float:
    return shape.get_area()