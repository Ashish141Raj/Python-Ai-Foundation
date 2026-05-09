# Search for number in 2D grid; break when found.

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = int(input("Enter Number that you want to found: "))
found = False
for i in grid:
    for j in i:
        if j == target:
            print("found: ",j)
            found = True
            break
    if found:
        break