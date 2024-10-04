def classifyTriangle(a, b, c):
    """
    This function returns a string that classifies a triangle based on the side lengths a, b, and c.

    The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Krinal Akbari

    return:
        - 'Equilateral': if all three sides are equal
        - 'Isosceles': if exactly two sides are equal
        - 'Scalene': if no sides are equal
        - 'NotATriangle': if the inputs do not form a valid triangle
        - 'Right': if the triangle is a right triangle
        - 'InvalidInput': if input values are out of bounds or invalid
    """

    # Check that inputs are integers
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    
    # Check for invalid input: sides should be between 1 and 200
    if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # Check if it's a valid triangle using the triangle inequality theorem
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Check for equilateral triangle
    if a == b == c:
        return 'Equilateral'
    
    # Check for right triangle using the Pythagorean theorem
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return 'Right'
    
    # Check for isosceles triangle (two sides are equal)
    if a == b or b == c or a == c:
        return 'Isosceles'
    
    # If none of the above, it's a scalene triangle (all sides are different)
    return 'Scalene'
