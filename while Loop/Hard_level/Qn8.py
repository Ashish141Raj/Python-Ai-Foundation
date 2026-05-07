'''1. Password validation loop

Keep asking user for password until correct password is entered.'''

correct_PSW = "AsNa141"
Password = " "

while Password != correct_PSW:
    Password = input("Enter password: ")
   
    if Password == correct_PSW:
        print("Validation Successfull")
    else:    
        print("Please enter correct password")