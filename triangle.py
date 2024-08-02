n=3
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for l in range(n+1,1,-1):
    for o in range(n-i):
        print(" ",end="")
    for p in range(2*i-1):
        print("*",end="")
    print()