'''1. Armstrong Number

Problem:

Check whether N is an Armstrong number (3-digit).

Input:

Integer N.

Output:

True or False.

Example:

Input: 153

Output:

True'''

N = int(input("Enter Number: "))
temp = N

digits = len(str(N))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit**digits
    temp //= 10
    
if total==N:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")