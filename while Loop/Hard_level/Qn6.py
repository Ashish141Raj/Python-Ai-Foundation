'''Find LCM using while
Input:4 6
Output:12
'''
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))

i = 1
while n1 >= i and n2 >= i:
        if n1 % i == 0 and n2 % i == 0:
            LCM = i
        i += 1
print(f"LCM of {n1} and {n2} is: {LCM}")