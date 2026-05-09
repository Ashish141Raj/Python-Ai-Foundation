'''Nested loop: Stop inner loop when j == 3
Output:
12
12
12'''

for i in range(1,4):
    for j in range(1,i+2):
        if j == 3: break
        print(j,end="")
    print()