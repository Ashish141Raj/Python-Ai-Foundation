# Calculate the electricity bill based on the slab rates.

unit = int(input('Enter the units consumed by the Consumer: '))

if unit <= 100:
    bill = unit * 1.5
elif unit <= 200:
    bill = (100 * 1.5) +(unit - 100)*2.5
else:
    bill = (100*1.5)+(100*2.5)+(unit - 200)*4
print("Electricity bill= ",bill)