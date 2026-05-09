# Print pattern but skip middle row using continue.

for i in range(1,4):
    for j in range(1,i+2):

        if i == 2: continue
        print(j,end="")
    print()