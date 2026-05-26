'''1. Anagram Check
    
    Problem: Check whether strings `s1` and `s2` are anagrams.
Input:
s1 = "listen"
s2 = "silent"

Output:
true'''

s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

if sorted(s1) == sorted(s2):
    print("True")
else:
    print("False")