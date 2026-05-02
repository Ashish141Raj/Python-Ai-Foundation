'''1. Pyramid Pattern

---

Problem:

Given an integer N, print a centered pyramid of stars.

Input:

4

Output:  
   *
  ***
 *****
*******
'''

n = int(input("Enter Number: "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i - 1):
        print("*",end="")
    print()