'''Print all odd numbers up to N'''

n = int(input("enter number: "))

i = 1
while i <= n:
    if i % 2 != 0:
        print(i,end=" ")
    i += 1
