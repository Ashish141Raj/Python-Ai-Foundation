'''1. Palindrome Number

Problem:

Check whether N is palindrome.

Input:

Integer N.

Output:

True or False.

Example:

Input: 121

Output:

True'''

num = int(input("Enter a Number: "))
temp = num

rev = 0
for i in range(len(str(num))):
    digit = num % 10
    rev = rev*10 + digit 
    num //= 10

if temp == rev:
    print("palindrome Number/True")
else:
    print("Not palindrome Number/False")