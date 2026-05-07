'''1. Menu-driven calculator

Keep showing menu until user selects Exit.
1. Add
2. Subtract
3. Multiply
4. Exit'''

while True:
    print("1. Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        n1 = int(input("Enter n1: "))
        n2 = int(input("Enter n2: "))

        Add = n1 + n2
        print(f"{n1} + {n2} = {Add}")

        break
    elif choice == "2":
        n1 = int(input("Enter n1: "))
        n2 = int(input("Enter n2: "))


        sub = n1 - n2
        print(f"{n1} - {n2} = {sub}")

        break
    elif choice == "3":
        n1 = int(input("Enter n1: "))
        n2 = int(input("Enter n2: "))

        mul = n1 * n2
        print(f"{n1} * {n2} = {mul}")

        break
    elif choice == "4":
        print("calculator Closed")
        
        break
    else:
        print("Invalid Choice")