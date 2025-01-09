# Program - if age>18 -allowed to vote
# else -> not allowed to vote
from traceback import print_tb

user_age = int(input("Please enter the age of the user\n"))

# if user_age>18:
#     print("Yes you can go yo goa and vote")
# else:
#     print("Not yo can't go and can't vote")

#######################################

# with the help of Ternary Operator

print("Yes you can go yo goa and vote" if user_age>18 else "Not yo can't go and can't vote")