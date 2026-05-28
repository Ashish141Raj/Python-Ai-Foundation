'''1. Longest Word
    
    Problem: Return longest word in sentence `s`.
Input:
s = "I love programming"

Output:
"programming"'''

s = input("Enter a sentence: ")
words = s.split()

lng_sen = " "

for word in words:
    if len(word) > len(lng_sen):
        lng_sen = word
print(lng_sen)
