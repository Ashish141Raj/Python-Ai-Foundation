'''1. Largest Digit

Problem:

Find largest digit in N.

Input:

Integer N.

Output:

Largest digit.

Example:

Input: 5482

Output:

8'''

N = int(input("Enter Number: "))
Temp = N

max_digit = 0
while Temp > 0:
    digit = Temp % 10

    if digit > max_digit:
        max_digit = digit
    Temp //=10

print("Maximum digit is: ",max_digit)
