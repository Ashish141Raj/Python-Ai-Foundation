'''1. Reverse Words
    
    Problem: Reverse the order of words in a sentence.
Input:
s = "I love Python"

Output:
"Python love I"'''

sen = input("Enter a sentence: ")

broke_sen = sen.split()

rev = " "

for i in range(len(broke_sen)-1 , -1, -1):
    rev += broke_sen[i]+" "

print(rev)
