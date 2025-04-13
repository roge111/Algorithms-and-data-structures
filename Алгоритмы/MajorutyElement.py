def majorityElement(nums):
    n = len(nums)
    count = n/3
    hash = {}
    result = []
    
    for number in nums:
        if number not in hash:
            hash[number] = 1
            if hash[number] > count:
                result.append(number)
        elif hash[number] > count:
            continue
        elif hash[number] + 1 > count:
            hash[number] += 1
            result.append(number)
        else:
            hash[number] += 1
    return result

print(majorityElement([1]))