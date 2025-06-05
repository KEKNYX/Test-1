import unittest
from geometry import Circle, Triangle


class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.get_area(), 28.274333882308138, delta=1e-9)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.get_area(), 6.0, delta=1e-9)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 5)

    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 3)

    def test_right_triangle_check(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

        triangle2 = Triangle(5, 5, 5)
        self.assertFalse(triangle2.is_right_triangle())


if __name__ == '__main__':
    unittest.main()