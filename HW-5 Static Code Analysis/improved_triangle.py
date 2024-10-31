"""
Module to classify types of triangles based on side lengths.
"""

def classify_triangle(side_a, side_b, side_c):
    """
    Classifies a triangle based on the side lengths side_a, side_b, and side_c.

    Returns:
        str: One of the following classifications:
            - 'Equilateral': if all three sides are equal
            - 'Isosceles': if exactly two sides are equal
            - 'Scalene': if no sides are equal
            - 'NotATriangle': if the inputs do not form a valid triangle
            - 'Right': if the triangle is a right triangle
            - 'InvalidInput': if input values are out of bounds or invalid
    """

    def is_valid_input():
        """Checks if inputs are integers and within the range of 1 to 200."""
        return all(isinstance(x, int) and 1 <= x <= 200 for x in (side_a, side_b, side_c))

    def is_valid_triangle():
        """Checks if the side lengths form a valid triangle."""
        return (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a)

    def is_right_triangle():
        """Checks if the triangle is a right triangle."""
        return (side_a**2 + side_b**2 == side_c**2 or side_a**2 + side_c**2 == side_b**2 or side_b**2 + side_c**2 == side_a**2)


    if not is_valid_input():
        return 'InvalidInput'
    if not is_valid_triangle():
        return 'NotATriangle'
    if side_a == side_b == side_c:
        return 'Equilateral'
    if is_right_triangle():
        return 'Right'
    if side_a == side_b or side_b == side_c or side_a == side_c:
        return 'Isosceles'

    return 'Scalene'  # Ensure there is a newline here
