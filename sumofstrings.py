s = "45ae23au1"
num = ''
l = []
for char in s:
    if char.isdigit():
        num += char
    else:
        if num:
            l.append(int(num))
            num = ''
if num:
    l.append(int(num))

print(l)
total = sum(l)
print(total)