'''1. Remove Duplicates
    
    Problem: Remove duplicate characters from string `s`.
Input:
s = "banana"

Output:
"ban"'''

s = input("Enter String: ")
result = " "

for i in s:
    if i not in result:
        result += i
print(result)