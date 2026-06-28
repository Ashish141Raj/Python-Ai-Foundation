# Print all Armstrong Number between 1 and 1000.
for i in range(1,1001):
    sum = 0
    temp = i
    digits = len(str(i))

    while temp > 0:
        digit = temp % 10
        sum += digit**digits
        temp //= 10
    if sum == i:
        print(i,end=" ")

