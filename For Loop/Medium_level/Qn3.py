'''1. Prime Check

Problem:

Determine if N is prime.

Input:

Integer N.

Output:

True or False.

Example:

Input: 7

Output:

True'''

N = int(input("Enter Number: "))

isPrime = True

if N <= 1:
    isPrime = False
else:
    for i in range(2,N):
        if N % i == 0:
            isPrime = False
            break
print(isPrime)
        