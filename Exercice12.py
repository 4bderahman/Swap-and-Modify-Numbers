# Input the first number
x = float(input("Please enter the 1st number: "))

# Input the second number
y = float(input("Please enter the 2nd number: "))

# Check if the product of the two numbers is positive
if x * y > 0:
    z = x
    x = y
    y = z
else:
    x = x + y
    y = x * y

print("The 1st value is now:", x)
print("The 2nd value is now:", y)
