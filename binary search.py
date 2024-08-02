import random

ra = [random.randint(1, 10) for i in range(6)]
ra.sort()
so = ra
print("Sorted list:", so)

l = 0
r = len(so) - 1
target = int(input("Enter target: "))

while l <= r:
    m = (l + r) // 2
    if so[m] == target:
        print("Element Found")
        break
    elif target > so[m]:
        l = m + 1
    else:
        r = m - 1
else:
    print("Element not found")
