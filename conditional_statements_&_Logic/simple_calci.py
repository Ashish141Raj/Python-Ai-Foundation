# Create a menu-driven calculator using match-case(switch-case) to perform addition,subtraction,multiplication, and division.
num1 = int(input("Enter value of num1: "))
num2 = int(input("Enter value of num2: "))

op = input("Enter operation choice(+,-,*,/): ")

match op:
    case '+':
        print(num1," + ",num2, "=",(num1+num2))
    case '-':
        print(num1," - ",num2, "=",(num1-num2))
    case '*':
        print(num1," * ",num2, "=",(num1*num2))
    case '/':
        print(num1," / ",num2, "=",(num1/num2))