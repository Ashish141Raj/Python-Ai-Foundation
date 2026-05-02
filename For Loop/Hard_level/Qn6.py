'''1. Reverse Pyramid

---

Problem:

Given an integer N, print an inverted centered pyramid.

Input:

4

Output:

*******
 *****
  ***
   *
'''
n = int(input("enter num: "))

for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for j in range(2*(n-i)+1):
        print("*",end="")
    print()
