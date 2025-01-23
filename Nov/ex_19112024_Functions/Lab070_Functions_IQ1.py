# Wap to sum of three number from the user input
# if user didn't use any number than use default as 100, 200, 300

num1 = int(input("Enter the num1:"))
num2= int(input("Enter the num2:"))
num3= int(input("Enter the num3:"))

def sum_three(n1=100,n2=200,n3=300):
    return n1+n2+n3

result1 = sum_three(num1,num2,num3)
print("Addition is",result1)

result2 = sum_three()
# result2 = sum_three(10)
# result2 = sum_three(10,20)
# result2 = sum_three(10,20,30)
print(result2)