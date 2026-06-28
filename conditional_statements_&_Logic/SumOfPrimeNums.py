# Fidn the sum of all prime numbers between 1 and N.

num = int(input("Enter Number: "))
sum = 0

for n in range(2,num+1):
    is_prime = True

    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        sum +=n
print("sum of all prime numbers are: ",sum)

