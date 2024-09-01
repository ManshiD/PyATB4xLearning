# User Defined
# 1. They cant return something -> non return
# 2. They can return something
# They have parameters
# They dont have parameters / arguments

# Example 1. They cant return something -> non return
# No Return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello World")

result=greet()
print(result)

# 2. No Return Type and with Argument
def greet_by_name(name): # name -> variable name, argument / parameter
    print("Hello, ", name)

greet_by_name("Pramod")

# 3. No Return Type and with default Argument
def say_hello_default_arg(name="Manshi"):
    print("Hello, ", name)

say_hello_default_arg("Amit")
say_hello_default_arg()
say_hello_default_arg(name="Radhika") # positional argument

def multiple_args(name1="Manshi1", name2="Manshi2", name3="Manshi3"):
    print("Multiple Arguments, ", name1, name2, name3)

multiple_args(name1="Ram", name2="Yunus", name3="Deepshikha")
multiple_args(name1="PRACHI")

# 4. Argument + Return Type
def sum_of_two_number(num1, num2):
    return (num1+num2)

def sum_of_two_number_with_default(num1=100, num2=200):
    return (num1+num2)

# result=sum_of_two_number(10, 34)
result=sum_of_two_number(num1=34, num2=34)
print(result)

result2=sum_of_two_number_with_default()
print(result2)