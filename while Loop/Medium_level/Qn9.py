# Convert decimal to binary

n = int(input("Enter Number: "))

binary = " "

while n > 0:
    rem = n % 2
    binary = str(rem) +" "+binary
    n //= 2
print("Binary: ",binary)
