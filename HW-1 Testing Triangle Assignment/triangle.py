#create the function
def classify_triangle(a, b, c):
    
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        3
        return "Not a valid triangle"

    #Condition to check if triangle is right angle or not
    is_right_triangle = (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)
    
    #Check type of Traingle
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    #check if triangle is Equilateral or Isosceles or Scalene triangle and Right angle
    if is_right_triangle:
        return f"{triangle_type} and Right Triangle"
    else:
        return triangle_type

#Defining triangle sides measurement 
a = 2
b = 3
c = 4
#Calling the function
print(classify_triangle(a, b, c))

