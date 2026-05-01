'''1. Count Vowels

Problem:

Given a string S, count number of vowels.

Input:

String S.

Output:

Integer count.

Example:

Input: hello

Output:

2'''

string = input("Enter string: ")

countVowel = 0
for str in string:
    if str == 'a' or str =='A':
        countVowel +=1
    elif str == 'e' or str == 'E':
        countVowel += 1
    elif str == 'i' or str == 'I':
        countVowel += 1
    elif str == 'o' or str == 'O':
        countVowel +=1
    elif str == 'u' or str == 'U':
        countVowel +=1
print("Vowels in ",string,"are: ",countVowel)