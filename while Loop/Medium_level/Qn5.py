'''Print all factors of N'''
n = int(input("enter number: "))


i = 1
while i <= n:
    if n % i == 0:
        print(i,end=" ")
    i += 1