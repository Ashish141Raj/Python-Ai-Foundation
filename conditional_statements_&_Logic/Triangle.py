# Check whether three sides can form a valid triangle. if Yes,It is Equilateral,Isosceles,or Scalene.

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        print("Eqilateral Triangle")
    elif a==b or b==c or c==a:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")