'''1. Count Consonants
    
    Problem: Count total consonants in `s`.
Input:
s = "hello"

Output:
3'''

s = input("Enter string: ")

count = 0
for ch in s:
    if ch.isalpha()  and ch.lower() not in "aeiou":
        count += 1
print(count)