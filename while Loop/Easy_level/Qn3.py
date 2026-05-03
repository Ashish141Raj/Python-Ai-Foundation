'''Print all even numbers up to N'''

N =int(input("enter a number: "))

i=1
while i <= N:
    if i % 2 == 0:
        print(i)
    i += 1