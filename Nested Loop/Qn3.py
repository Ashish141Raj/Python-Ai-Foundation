'''Print triangle but skip number 2 using continue
Output:
1
13
134'''
for i in range(1,4):
    for j in range(1,i+2):
        if j == 2: continue
        print(j,end="")
    print()