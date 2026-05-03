'''Print Fibonacci series up to N term'''

n = int(input("Enter Number: "))

a = 0 
b = 1

i = 1
while i <= n:
    print(a,end=" ")
    c = a+b
    a = b
    b = c
    i += 1