'''1. Count Uppercase and Lowercase

Problem:

Given string S, count uppercase and lowercase characters.

Input:

String S.

Output:

Two integers.

Example:

Input: PyThOn

Output:

Uppercase: 3

Lowercase: 3'''

str = input("Enter str: ")

upper = 0
lower = 0

for i in str:
    if i >= 'A' and i <= 'Z':
        upper +=1
    elif i >= 'a' and i <= 'z':
        lower+=1
print("uppercase: ",upper)
print("Lowercase: ",lower)