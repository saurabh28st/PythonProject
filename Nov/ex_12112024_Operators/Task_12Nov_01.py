# Write a program to take a user age and let him know if he can go to the club
from traceback import print_tb

age = int(input("Please enter the age :"))

if age<21:
    print("He can't go to the club")
else:
    print("He can go to the club")