def frequencySort(nums):
    from collections import Counter
    freq = Counter(nums)
    nums.sort(key=lambda x: (freq[x], -x))
    return nums

print(frequencySort([9, 9, 4, 4, 5, 5, 5])) 
