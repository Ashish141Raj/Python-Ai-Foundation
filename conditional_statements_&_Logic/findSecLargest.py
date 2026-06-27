# Find the Second Largest among three numbers without using sorting.

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

if(a>b and a<c) or (a<b and a>c):
    print("second largest num: ",a)
elif(b>a and b<c) or (b<a and b>c):
    print("second largest num: ",b)
else:
    print("Second largest num: ",c)
