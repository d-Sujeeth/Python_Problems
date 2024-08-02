a = input("Enter 1st name: ")
b = input("Enter seconfd name: ")
l1 = list(a)
l2 = list(b)
common_chars = []

for i in l1:
    if i in l2:
        common_chars.append(i)

for char in common_chars:
    print(char,end=" ")

