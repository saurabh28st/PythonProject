# Take 2 numbers from the user and print the Quotient and Reminder

num1 = int(input("Please enter the first number (dividend) :"))
num2 = int(input("Please enter the second number (divisor) :"))

quotient = num1//num2
# print(quo)
print("Quotient is :",quotient)

remainder = num1%num2
print("Reminder is :",remainder)

# In this program we can use the divmod()