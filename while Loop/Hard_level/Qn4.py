'''Print number palindrome pattern
Input:4
Output:
1
121
12321
1234321
'''
n = int(input("Enter Number: "))

i = 1
while i <= n:

    j = 1
    while j <= i:
        print(j,end=" ")
        j+=1

    j = i - 1
    while j >= 1:
        print(j,end=' ')
        j-=1
    print()
    i+=1