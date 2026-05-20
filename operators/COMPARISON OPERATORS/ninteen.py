# 19.Take two numbers and check which one is bigger.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if num1 > num2:
    print(F"{num1} is greater")
elif num2 > num1:
    print(F"{num2} is greater")
else:
    print("Both are Equal")