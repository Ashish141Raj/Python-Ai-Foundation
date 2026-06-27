'''1. Replace Vowels
    
    Problem: Replace all vowels in `s` with '*'.
Input:
s = "hello"

Output:
"h*ll*"   '''

s = input("Enter a string: ")

for i in s:
    if i.lower() == 'aeiou':
        pass