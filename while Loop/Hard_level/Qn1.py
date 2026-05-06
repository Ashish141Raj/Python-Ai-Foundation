# Print reverse pattern
'''
Input:4
Output:
****
***
**
*
'''
n = int(input("Enter pattern Number: "))

i = n
while i >= 1:
    print("*" * i)
    i -= 1