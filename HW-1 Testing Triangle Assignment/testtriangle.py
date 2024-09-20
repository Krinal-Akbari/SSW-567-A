
import unittest
from triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):

    #Test case for equilateral triangle
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")

    #Test case for isosceles triangle
    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles")
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles")

    #test case for scalene triangle
    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right Triangle")
        self.assertEqual(classify_triangle(5, 7, 9), "Scalene")
    
    #Test case for right angle triangle
    def test_right_angle_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right Triangle")
        self.assertEqual(classify_triangle(6, 8, 10), "Scalene and Right Triangle")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene and Right Triangle")
    
    #test case for not a triangle
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a valid triangle")
        self.assertEqual(classify_triangle(5, 1, 1), "Not a valid triangle")
    
    #test case for isosceles and right triangle
    def test_isosceles_right_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 2**0.5), "Isosceles and Right Triangle")
    
    def test_invalid_input(self):
        self.assertEqual(classify_triangle(0, 0, 0), "Not a valid triangle")
        self.assertEqual(classify_triangle(-3, 4, 5), "Not a valid triangle")
        self.assertEqual(classify_triangle(3, -4, 5), "Not a valid triangle")
        self.assertEqual(classify_triangle(3, 4, -5), "Not a valid triangle")

if __name__ == '__main__':
    unittest.main()
