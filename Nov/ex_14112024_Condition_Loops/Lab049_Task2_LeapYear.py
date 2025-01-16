# WAP to find Leap Year
# Leap year is multiple by 4, except of year every divisible by 100 but not by 400
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400

year = int(input("Please enter the year to find leap year"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year is leap year")
else:
    print("The year isn't a leap year")
