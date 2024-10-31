# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Krinal Akbari
"""

import unittest
from improved_triangle import classify_triangle


class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangle(self):
        self.assertEqual(classify_triangle(5, 5, 8), 'Isosceles', '5,5,8 should be isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(7, 8, 9), 'Scalene', '7,8,9 should be scalene')
    
    def testNotATriangle(self):
        self.assertEqual(classify_triangle(1, 10, 12), 'NotATriangle', '1,10,12 is not a triangle')
    
    def testInvalidInputNegative(self):
        self.assertEqual(classify_triangle(-1, 2, 3), 'InvalidInput', '-1,2,3 should be invalid input')
        
    def testInvalidInputZero(self):
        self.assertEqual(classify_triangle(0, 2, 3), 'InvalidInput', '0,2,3 should be invalid input')

    def testLargeValues(self):
        self.assertEqual(classify_triangle(201, 150, 300), 'InvalidInput', '201,150,300 should be invalid input')

    def testFloatingPointInput(self):
        self.assertEqual(classify_triangle(3.5, 4, 5), 'InvalidInput', '3.5,4,5 should be invalid input')

    def testDegenerateTriangle(self):
        self.assertEqual(classify_triangle(5, 5, 10), 'NotATriangle', '5,5,10 is a degenerate triangle')

    def testStringInput(self):
        self.assertEqual(classify_triangle("2", "4", "5"), 'InvalidInput', "'2','4','5' should be invalid input'")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

