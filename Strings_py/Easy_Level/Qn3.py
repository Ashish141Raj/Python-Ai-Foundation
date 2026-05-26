'''1. Count Vowels
    
    Problem: Count total vowels in string `s`.
Input:
s = "hello"

Output:
2'''

s = input("Enter string: ")

count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count +=1
print(count)