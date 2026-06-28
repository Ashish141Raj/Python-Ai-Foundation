# Write a program to calculate the factorial of a number using a while number.

num = int(input("Enter value of Num: "))

# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print(fact)
fact = 1
while num > 0:
    fact = fact * num
    num -= 1
print(fact)