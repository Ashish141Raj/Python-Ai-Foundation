'''1. Reverse a Number

Problem:

Reverse digits of integer N.

Input:

Integer N.

Output:

Reversed number.

Example:

Input: 123

Output:

321'''

# N = input("Enter Number: ")


# reverse = " "
# for i in N:
#     reverse = i + reverse
# print("Reverse of ",N," is: ",reverse)

N = int(input("Enter Number: "))
Temp = N

rev = 0
while Temp > 0:
    digit = Temp % 10
    rev = rev*10 + digit
    Temp //= 10
print("Reverse: ",rev)