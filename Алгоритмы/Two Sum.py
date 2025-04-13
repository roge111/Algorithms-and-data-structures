def twoSum(nums, target):
    hash = {}

    for index, num in enumerate(nums):
        x = target - num
        if x in hash:
            return [index, hash[x]]
        hash[num] = index

print(twoSum([-3,4,3,90], 0))