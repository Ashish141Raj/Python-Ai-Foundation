'''1. Count Spaces
    
    Problem: Return number of spaces in string `s`.
Input:
s = "hello world"

Output:
1'''

s = input("Enter string: ")

count = 0

for ch in s:
    if ch == " ":
        count += 1
print(count)