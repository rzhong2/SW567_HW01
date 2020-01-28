import unittest
from classify import classify_triangle
class NamesTestCase(unittest.TestCase):
    def right_triangle(self):
        formatted_name=classify_triangle(3,4,5)
        self.assertEqual(formatted_name,'right triangle')
    def equilateral_triangle(self):
        formatted_name=classify_triangle(3,3,3)
        self.assertEqual(formatted_name,'equilateral triangle')
    def scalene_triangle(self):
        formatted_name=classify_triangle(3,4,6)
        self.assertEqual(formatted_name,'scalene triangle')
    def isosceles_triangle(self):
        formatted_name=classify_triangle(3,3,5)
        self.assertEqual(formatted_name,'isosceles triangle')

unittest.main(argv=['first-arg-is-ignored'], exit=False)
