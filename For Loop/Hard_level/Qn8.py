'''1. Hollow Pyramid Pattern

---

Problem:

Print a hollow pyramid of height N.

Input:

4

Output:
   *
  * *
 *   *
*******
'''
n = int(input("Enter num: "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")

    for j in range(1, 2*i):
        if j ==1 or j == 2*i-1 or i == n:
            print("*", end="")
        else:
            print(" ",end="")
    print() 