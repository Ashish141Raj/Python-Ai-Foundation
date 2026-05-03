'''Print factorial of N'''

N = int(input("Enter Number: "))

fact = 1
i = 1
while i <= N:
    fact = fact * i
    i += 1
print(fact)
