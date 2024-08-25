"""
Grade Calculator:
Write a program that calculates and displays the letter grade for a given numerical score
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
"""

# Logic Building Formula

# 1 -> User Inputs -> score or marks -> int
# 2 -> O/P -> str -> A or B

score = int(input("Enter your score\n"))
grade = "F"
# score >= 90  and score <= 100 -> "A"
# score >= 80  and score <= 89 -> "B"

if 90 <= score <= 99:   # Simplified Chaining Format -> 90 <= score >= 100
    print("Your grade is", "A")
elif 80 <= score <= 89:
    print("Your grade is", "B")
elif 70 <= score <= 79:
    print("Your grade is", "C")
elif 60 <= score <= 69:
    print("Your grade is", "D")
elif score >= 100:
    print("Your are Superman!")
else:
    print("Your grade is", "F")
