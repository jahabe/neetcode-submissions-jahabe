class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        global_max = nums[0]

        for num in nums[1:]: 
            candidates = [num, current_max * num, current_min * num]
            current_max = max(candidates)
            current_min = min(candidates)

            global_max = max(global_max, current_max)
        return global_max