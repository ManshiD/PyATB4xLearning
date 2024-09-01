# Create a program to sum of three number from the user input

num1 = int(input("Enter number1 : ")) #100
num2 = int(input("Enter number2 : ")) #200
num3 = int(input("Enter number3 : ")) #300

def sum_of_three_number(n1, n2, n3): # (100, 200, 300)
    return n1 + n2 + n3 # 100 + 200 + 300 so total = 600

result1 = sum_of_three_number(num1, num2, num3)
print(result1)

result2 = sum_of_three_number(n1=num1, n2=num2, n3=num3)
print(result2)