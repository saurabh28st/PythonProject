# WAP to find max number using via If Else

num1 = float(input("Enter the num1 :"))
num2 = float(input("Enter the num2 :"))

if num1 >= num2:
    print("Max is ",num1)
else:
    print("max is ",num2)

# Edge Cases - num1 == num2 -> Handled.
# String -> ABC, ten -> try and catch
# -ve values