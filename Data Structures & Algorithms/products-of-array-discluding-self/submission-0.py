class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        out = [1] * n

        pref = 1
        for i in range(n): 
            out[i] = pref
            pref *= nums[i]
        
        suff = 1
        for i in range(n-1,-1,-1): 
            out[i] *= suff
            suff *= nums[i]

        return out