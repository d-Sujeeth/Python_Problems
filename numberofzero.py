str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

set1 = set(str1)
set2 = set(str2)

common_elements = set1 & set2

result1 = ''.join([char for char in str1 if char not in common_elements])
result2 = ''.join([char for char in str2 if char not in common_elements])

new_string = result1 + result2

print("New string without common elements:", new_string)
