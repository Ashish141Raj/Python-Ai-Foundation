'''1. Factorial

Problem:

Compute factorial of N using loop.

Input:

Integer N.

Output:

Factorial value.

Example:

Input: 5

Output:

120'''

N = int(input("Enter a Number: "))

fact = 1
for i in range(1,N+1):
    fact *= i

print("Factorial of ",N," is: ",fact)