'''Count digits in a number'''

n = int(input("Enter Num: "))

count = 0
while n > 0:
    n //= 10
    count += 1
print(count)