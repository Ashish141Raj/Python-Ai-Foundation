'''Sum of digits'''

n = int(input("Enter a Number: "))

sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print(sum)