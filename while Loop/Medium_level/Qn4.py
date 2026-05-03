'''Check if number is prime'''

n = int(input("enter Number: "))


i = 2
is_prime = True

while i < n:
    if n % i == 0:
        is_prime = False
        break
    i += 1
 
if n <= 1:
    print("Not prime")
elif is_prime:
    print("prime")
else:
    print("not Prime")