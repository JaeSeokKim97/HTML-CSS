for i in range(1, 11):
    for j in range(10 - i):
        print(" ", end="")
    for j in range(1, i*2, 1):
        print("*", end="")
    print("")    

for i in range(10):
    for j in range(i):
        print(' ',end="")
    for j in range(20,1+i*2,-1):
        print('*',end="")
    print('')