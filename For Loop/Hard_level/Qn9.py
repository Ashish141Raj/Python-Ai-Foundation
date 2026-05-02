'''1. Right-Aligned Increasing Pattern

---

Problem:

Print a right-aligned increasing star pattern.

Input:

4

Output:
   *
  **
 ***
****
'''
n = int(input("enter num: "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
    