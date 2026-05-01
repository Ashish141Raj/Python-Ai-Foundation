'''
1. Reverse Counting

Problem:

Print numbers from N down to 1.

Input:

Integer N.

Output:

N to 1.

Example:

Input: 5

Output:

5 4 3 2 1
'''
N = int(input("Enter a Number: "))

for i in range(N,0,-1):
    print(i,end=" ")