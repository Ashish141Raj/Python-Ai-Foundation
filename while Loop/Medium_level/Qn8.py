# Calculate power without using ** operator

a = int(input("enter base: "))
b = int(input("enter power: "))

result = 1

i = 1
while i <= b:
    result = result * a
    i += 1

print("answer: ",result)
