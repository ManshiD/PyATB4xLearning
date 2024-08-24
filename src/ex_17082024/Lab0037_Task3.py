"""
Task #3
Explain the difference between the = operator and the == operator in Python.
What does the ** operator do in Python, and how is it used?
What does the ^ operator do in Python, and in what context is it commonly used?
"""""

# Explain the difference between the = operator and the == operator in Python. ?? Answer is:
# The = operator is used for assignment, such as when assigning a value to a variable.
# The == operator is the relational operator for checking equality of two values.

a = 300
b = 20
if b > a:
    print("b is greater than a")
elif a == b:                            # boolean
    print("a and b are equal")
else:
    print("a is greater than b")

# What does the ** operator do in Python, and how is it used ?? Answer is:
# raise the first operand to power of second

x = 3
y = 5

print(x ** y) # same as 3*3*3*3*3

""""
**: exponentiation
^: exclusive-or (bitwise)
%: modulus
//: divide with integral result (discard remainder)

"""""

# What does the ^ operator do in Python, and in what context is it commonly used ?? Answer is:
# The XOR or exclusive is a Boolean logic operation widely used in cryptography and
# generating parity bits for error checking and fault tolerance

print(6 ^ 3)  # output : 5     type int
print(6 ^ 9)  # output : 15

"""
The ^ exclusive-or (bitwise) operator compares each bit and set it to 1 if only one is 1, 
otherwise (if both are 1 or both are 0) it is set to 0:


6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
8 = 0000000000001000
9 = 0000000000001001
10= 0000000000001010
11= 0000000000001011
12= 0000000000001100
13= 0000000000001101
14= 0000000000001110
15= 0000000000001111
"""