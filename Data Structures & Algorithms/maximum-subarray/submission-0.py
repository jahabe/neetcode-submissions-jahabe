class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        result = nums[0]

        for i in range(1, len(nums)): 
            if current < 0: 
                current = nums[i]
            else: 
                current += nums[i]
            result = max(result, current)
        return result