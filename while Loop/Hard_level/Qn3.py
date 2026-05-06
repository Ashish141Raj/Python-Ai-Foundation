'''Print number triangle
Input:4
Output:
1
12
123
1234
'''

n = int(input("Enter Number: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j,end=" ")
        j += 1

    print()
    i += 1