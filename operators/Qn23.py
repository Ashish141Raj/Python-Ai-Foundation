# 23.Take price and discount %, calculate final price.

price = float(input("Enter Price of object: "))
discount = float(input("Enter Discount percent: "))

discount = (price*discount)/100
final_price = price - discount

print(f"final price of object = {final_price}")

