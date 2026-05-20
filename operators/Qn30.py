# 30.Take total bill and number of people, calculate per person share.

total_bill = float(input("Enter Amount of total bill: "))
person = int(input("Enter total number of persons: "))

share_on_per_person = total_bill/person
print(f"per person share of {total_bill} = {share_on_per_person}")