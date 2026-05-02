'''1. Perfect Number

Problem:

Check whether N is perfect (sum of proper divisors equals number).

Input:

Integer N.

Output:

True or False.

Example:

Input: 6

Output:

True'''

num = int(input("Enter a Number: "))

sum = 0
for i in range(1,num):
    if num % i == 0:
        sum +=i
if num == sum:
    print("perfect Number/True")
else:
    print("Not Perfect/False")