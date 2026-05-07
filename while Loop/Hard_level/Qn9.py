'''1. Banking simulation

Keep deducting withdrawal until balance becomes insufficient.'''

balance = 6000000

while balance > 0:
    withdrawl = int(input("Enter Withdrawl Amount: "))

    if balance >= withdrawl:
        balance = balance - withdrawl

        print("Remaining Balance: ",balance)
        
        exit = input("Press 1 to Exit or press anything to continue: ")

        if exit == "1":
            break
        else:
            continue

    else:
        print("Insufficient Balance")
        break
print("Execution Ends")
