'''Check if number is palindrome'''

n = int(input("Enter Number: "))
temp = n

rev = 0 
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
if temp == rev:
    print("palindrome")
else:
    print("Not palindrome")