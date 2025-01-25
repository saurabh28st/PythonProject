# Triangle Classifier

def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            print("Not a triangle")
    else:
        print("Not a valid length")


side1 = int(input("Enter the first side:"))
side2 = int(input("Enter the second side:"))
side3 = int(input("Enter the third side:"))

result2 = classify_triangle(side1, side2, side3)
print(f"The triangle is classified as: {result2}")
