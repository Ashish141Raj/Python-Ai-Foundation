'''Print centered pyramid (while loop only)
Input:4
Output:
*
***
*****
*******
'''
n = int(input("Entetr size of Pattern: "))

i = 1

while i <= n:
    print("*" *(2*i -1))
    i += 1
