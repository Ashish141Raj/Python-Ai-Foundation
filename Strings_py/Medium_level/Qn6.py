'''1. Count Uppercase & Lowercase
    
    Problem: Count uppercase and lowercase letters.
Input:
s = "PyThOn"

Output:
Uppercase: 3
Lowercase: 3'''

str = input("Enter string: ")

count_upper = 0
count_lower = 0

for ch in str:
    if ch.isupper():
        count_upper += 1
    elif ch.islower():
        count_lower += 1
print("UpperCase char is: ",count_upper)
print("LowerCase char is: ",count_lower)