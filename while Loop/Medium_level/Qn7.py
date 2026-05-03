'''Count frequency of a digit in number'''

n = int(input("Enter Number: "))
d = int(input("enter Digit: "))

count_frequency = 0
while n > 0:
    digit = n % 10 
    if digit  == d:
        count_frequency += 1
    n //= 10
print("Count frequency: ",count_frequency)