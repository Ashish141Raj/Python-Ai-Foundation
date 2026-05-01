'''
1. Sum of First N Numbers

Problem:

Given N, compute the sum of numbers from 1 to N.

Input:

Integer N.

Output:

Single integer representing the sum.

Example:

Input: 5

Output:

15

'''

N = int(input("Enter a Number: "))
sum = 0
for i in range(1, N+1):
    sum +=i
print("Single integer representing the sum: ",sum)