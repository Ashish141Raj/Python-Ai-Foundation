'''1. Strong Number

Problem:

Check if N is Strong number (sum of factorial of digits equals number).

Input:

Integer N.

Output:

True or False.

Example:

Input: 145

Output:

True'''

num = int(input("Enter a Number: "))
temp = num

sum = 0
while num > 0:
    digit = num % 10

    fact = 1
    for i in range(1,digit+1):
        fact = fact*i
    sum += fact
    num //= 10
if temp == sum:
    print("True")
else:
    print("False")

