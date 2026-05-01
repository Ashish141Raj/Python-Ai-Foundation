'''
1. Sum of Digits

Problem:

Given N, find sum of its digits.

Input:

Integer N.

Output:

Sum of digits.

Example:

Input: 123

Output:

6
'''
N = int(input("Enter a num: "))

total = 0

while N > 0:
   digit = N % 10
   total += digit
   N //= 10
print("Sum of Digits: ",total)
