# Homework
# Create a program, take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div
# format your output with f("")

# Print maths operations task.
# Problem statement: Take user input of two numbers and perform the below operations
# 1. Add
# 2. Sub
# 3. Mul
# 4. Div
# 5. power of
# Format output with f{""}
print("You will be prompted for inputting 2 numbers. Please input higher number first and lower number second.")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
print("Maximum of two numbers is: ", f"{max(num1, num2):.0f}")
print("Sum of the given numbers is: ", f"{num1+num2:.0f}")
print("Difference of the given numbers is: ", f"{num1-num2:.0f}")
print("Multiplication of the given numbers is: ", f"{num1*num2:.0f}")
print("Division of the given number is: ", f"{num1/num2:.0f}")
print("Considering only whole number values, ", num1, "Raised to the power of", num2, "is: ", f"{pow(int(num1), int(num2))}" )
print("Integer values of first number: ", int(num1))
print("Integer values of first number: ", int(num2))
