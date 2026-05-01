'''
1. Count Even Numbers

Problem:

Given N, count how many even numbers exist between 1 and N.

Input:

Integer N.

Output:

Count of even numbers.

Example:

Input: 10

Output:

5

'''
N = int(input("Enter a Number: "))

count = 0
for i in range(1,N+1):
    if i%2==0:
        count +=1
print("Total even Numbers: ",count)