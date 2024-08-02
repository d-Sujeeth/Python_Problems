def selsort(num):
    l=len(num)
    for i in range(l):
        minindex=i
        for j in range(i+1,l):
            if (num[j]<num[minindex]):
                minindex=j
        temp=num[i]
        num[i]=num[minindex]
        num[minindex]=temp
        

num=[5,3,8,6,7,2]
selsort(num)
print(num)

