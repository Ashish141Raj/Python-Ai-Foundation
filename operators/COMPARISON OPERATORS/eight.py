# 8.Take two floats and compare them.

num1 = float(input("Enter value of num1: "))
num2 = float(input("Enter value of num2: "))

if num1 > num2:
    print(f"{num1} is grater")
elif num2 > num1:
    print(f"{num2} is grater")
else:
    print(f"{num1} and {num2} both are equal")