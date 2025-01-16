# Write a program to take a user age and let him know if he can go to the club age->21

# Logic Building formula

# Step 1
# user input i/p -> data type -> int
# o/p -> String -> user if he can go or not

# Step 2. Rough Logic (brute force)
# age > 21 -> print can go
# age < 21 -> print can't go

# Step 3. Write the logic
age = int(input("Please enter the age :"))

if age >= 21:
    print("Can go to the club")
else:
    print("Can't go to the club")

# Step 4. Check for the edge cases.
# We should consider edge cases such as:
# Negative ages or extremely high values -> program will break
# Non-numeric input -> ABC
# Age which is valid -> 150

# Step 5. Optimize the code.
# Handle all the edges.