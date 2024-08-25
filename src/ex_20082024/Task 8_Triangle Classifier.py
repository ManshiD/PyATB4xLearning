"""
Task #8
✅ Triangle Classifier:

https://github.com/PramodDutta/PyATB4xLearning/blob/main/src/tasks/img.png

Write a program that classifies a triangle based on its side lengths. 
Given three input values representing the lengths of the sides, 
determine if the triangle is equilateral (all sides are equal), 
isosceles (exactly two sides are equal), or scalene (no sides are equal). 
Use an if-else statement to classify the triangle.

"""""

side_length1 = int(input('Enter the length:\n'))
side_length2 = int(input('Enter the length:\n'))
side_length3 = int(input('Enter the length:\n'))

if side_length1 == side_length2 and side_length2 == side_length3:
    print('Equilateral triangle all sides are equal')
elif side_length1 == side_length2 or side_length1 == side_length3 or side_length2 == side_length3:
    print('Isoceles triangle exactly two sides are equal')
else:
    print('Scalene triangle no sides are equal')