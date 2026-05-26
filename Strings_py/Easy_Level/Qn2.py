'''1. Palindrome Check
    
    Problem: Determine whether a string `s` is a palindrome.
Input:
s = "madam"

Output:
true
'''
s = input("Enter string: ")

slicing = s[: :-1]

if s == slicing:
    print(f"{s} is Palindrome")
else:
    print(f"{s} is not Palindrome")