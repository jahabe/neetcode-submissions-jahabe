"""
Understanding: 
    - given: integer array num, integer target
    - return: the index location where the target number is 
    - example: target=1 and nums=[3,4,5,6,1,2]. We can see that the 1 is at nums[4] <- we are returning this. 
    - recommended compexity: 
        - O(log n) time 

Edge cases: 
    - No need to worry about the empty nums
    - No target number -> return -1

Possible approach: 
    - brute force: search all the numbers by iterating all, but it's not good solution because of time waste. 
    - binary search: 

Plan 1 - brute force:
    - for i in range(len(nums)): if nums[i] == target: return i else: return -1
    
plan 2 - binary search 
    - edge case: find targeting number, if no-> return -1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)): 
        #     if nums[i] == target: 
        #         return i 
        # return -1
        left = 0 
        right = len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2

            if nums[mid] == target: 
                return mid
            
            if nums[left] <= nums[mid]: 
                if nums[left] <= target < nums[mid]: # when the target is in left side
                    right = mid -1
                else: # when the target in in the left side
                    left = mid + 1
            else: # when sorted in right side 
                if nums[mid] < target <= nums[right]: 
                    left = mid + 1
                else: 
                    right = mid - 1
        return -1