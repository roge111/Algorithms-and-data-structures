def maxSubArray(self, nums):
        cur_sum = nums[0]
        max_sum = cur_sum
        if len(nums) == 1:
            return nums[-1]
        for index, num in enumerate(nums):
            if index == 0:
                continue
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
            
        return max_sum
