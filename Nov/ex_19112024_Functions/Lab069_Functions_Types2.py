# User Defined
# 1. Non-return type
# 2. Written type
# 3. They have parameter
# 4. They don't have parameters/arguments
from Nov.ex_07112024_keywords_identifier_variables.Lab014_Math_Functions import result

# Note: In case of python we don't need to define the function, In java we have to define the function

# 1. The can't return -> non return
# No Return type and No Parameter/Argument
def greet():
    print("Hello")
greet()

# 2. No return type and with Argument/Parameter
def greet_by_name(name):
    print("Hello",name)
greet_by_name("saurabh")

print("----------------------------")

# 3. No Return type but with default Argument       # Positional Argument
def say_hello_default_arg(name="Saurabh"):
    print("Hello",name.upper())
say_hello_default_arg("Tiwari")
say_hello_default_arg()


def multiple_args(name1="A",name2="B"):
    print("Mul",name1,name2)
multiple_args()
multiple_args("Lucky","Sharma")
multiple_args(name1="Saurabh")
multiple_args(name1="Sam",name2="Tiwari")


# 4. Argument + Return Type

def sum_of_two(a,b):
    return a + b

result = sum_of_two(4,56)
print(result)

def sum_of_two_number_with_default(num1=100, num2=200):
    return num1 + num2

result = sum_of_two_number_with_default(num1=34, num2=34)
print(result)
result = sum_of_two_number_with_default()
print(result)

