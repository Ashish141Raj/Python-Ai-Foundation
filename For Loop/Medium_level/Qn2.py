'''1. Fibonacci Series

Problem:

Print first N Fibonacci numbers.

Input:

Integer N.

Output:

Sequence.

Example:

Input: 5

Output:

0 1 1 2 3'''

N = int(input("Enter Number: "))

f = 0
s = 1
for i in range(N):
    print(f,end=" ")
    t = f + s
    f = s
    s = t
    