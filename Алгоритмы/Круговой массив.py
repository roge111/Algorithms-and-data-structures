def nextGreaterElements(nums: list) -> list:

    result = [-1] * len(nums)
    stack = []
    n = len(nums)
    for i in range(n * 2):
        num = nums[i % n]
        while stack and nums[stack[-1]] < num:
            index = stack.pop()
            result[index] = num
        if i < n:
            stack.append(i)
    return result



print(nextGreaterElements([1,2,3, 4, 5]))

