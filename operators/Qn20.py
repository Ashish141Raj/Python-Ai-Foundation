# 20.Take Total second and convert into miniute(use // and %)

seconds = int(input("Enter Total Second: "))

minute = seconds//60
remaining_second = seconds % 60

print(f"{seconds} seconds = {minute} minute and {remaining_second} sec")