# Wap to find Leap Year
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400

year = int(input("Please enter the year :"))

if year%4==0 and year%100 !=0 or year%400==0:
    print("Year is Leap Year")
else:
    print("Year is not a Leap Year")