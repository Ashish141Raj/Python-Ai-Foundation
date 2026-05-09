# Skip printing even numbers inside nested loop (use continue).
for i in range(1,4):
    for j in range(1,10):
        if j % 2 == 0: continue
        print(j,end="")
    print()