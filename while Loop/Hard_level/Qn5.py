'''Find GCD of two numbers using while loop
Input:
1218
Output:
6
'''
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

gcd = 1

i = 1
while n1 >= i and n2 >= i:
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
    i += 1
print(f"Hcf/GCD of {n1} and {n2} is:{gcd}")