def sort(n):
    R=len(n)
    for i in range(R-1,0,-1):
        for j in range(i):
            if n[j]>n[j+1]:
                temp=n[j]
                n[j]=n[j+1]
                n[j+1]=temp
    
n=[15,4,9,8,5,6]
sort(n)
print(n)
