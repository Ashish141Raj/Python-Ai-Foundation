'''1. Count Digits

Problem:

Given an integer N, count how many digits it contains.

Input:

Integer N.

Output:

Digit count.

Example:

Input: 12345

Output:

5'''
N = int(input("Enter Digits: "))

count = 0

while N > 0:
    N //= 10
    count +=1
print("digits it contains: ",count)
