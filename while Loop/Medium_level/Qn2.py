'''Check if number is Armstrong (3-digit)'''

n = int(input("Enter number: "))
temp = n

digits = len(str(n))

sum = 0
while n > 0:
    digit = n % 10
    sum += digit**digits
    n //= 10
if temp == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
