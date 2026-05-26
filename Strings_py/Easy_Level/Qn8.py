'''1. Character Frequency
    
    Problem: Count how many times character `c` appears in `s`.
Input:
s = "banana"
c = "a"

Output:
3'''

s = input("Enter a string: ")

c = input("Enter character to count: ")

count = 0

for ch in s:
    if ch == c:
        count += 1
print(count)