# Write a Python program to calculate the
# area of a circle given its radius using the formula
# area=pie*r^2 (Take pie as 3.14)

# Logic Building formula

# Step 1 Figure out inputs and outputs
# input -> r -> data type -> float
# pi -> 3.14, math.pi
# power -> pow or ** -> any

# o/p -> float - area, print area

# Step 2
# rough logic = area = 3.14 * pow(r,2)

# Step 3 - Write the logic
import math
radius = float(input("Enter the radius of the circle\n"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius, 2)
area2=3.14 * (radius**2)
print("Area of the circle is", area)
print(f"Area of the circle is, {area:.2f}")
print("Area of the circle is", area2)

# * - mul
# ** - power

print(3.141592653589793*(float(input("Enter the radius\n"))**2))