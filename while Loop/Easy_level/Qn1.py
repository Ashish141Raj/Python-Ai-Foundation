'''1. Print numbers from 1 to N

Problem:

Given an integer N, print numbers from 1 to N using a while loop.

Example:
Input:5
Output:12345
'''

n = int(input("enter Number: "))

i=1
while i<=n:
    print(i,end=" ")
    i +=1
