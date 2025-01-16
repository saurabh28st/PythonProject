# Triangle Classifier

side1 = float(input("Please enter the length of side1 :"))
side2 = float(input("Please enter the length of side2 :"))
side3 = float(input("Please enter the length of side3 :"))

if side1 == side2 and side2 == side3:
    print("Triangle is Equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")