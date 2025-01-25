# Wap that prints numbers from 1 to 100.
# However, of multiple of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz"
# For numbers that are multiples of both 3 and 5, print "FizzBuzz." (for, if)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
