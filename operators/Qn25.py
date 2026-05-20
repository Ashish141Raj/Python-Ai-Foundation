# 25.Take two numbers and print remainder without using % (use formula).
# Dividend=(Divisor × Quotient)+Remainder
# so Remainder = Dividend - (Divisor x Quotient)
# and Quotient = [Dividend//Divisor]


num1 = int(input("Enter value of num1: "))
num2 = int(input("Enter value of num2: "))

quotient = num1 // num2

remainder = num1-(num2 * quotient)
print(f"Quotient = {quotient}")
print(f"Remainder = {remainder}")