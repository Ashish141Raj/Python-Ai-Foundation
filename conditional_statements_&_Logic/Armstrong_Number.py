# Check whether a number is an Armstrong or not.

num = int(input("Enter a Number: "))
temp = num
power = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum += (digit**power)
    num //= 10
if sum == temp:
    print(temp," is Armstrong")
else:
    print(temp," is not a Armstrong")