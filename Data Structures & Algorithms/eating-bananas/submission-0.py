"""
Given: piles array integer
       piles[i]: # bananas in the ith pile 
       integer h: # hours you have to eat all the bananas

Return: minimum integer k you can eat all the bananas within h hours 

Edge cases: 
    - check if the pile exceeds integer h 
    - 

Plan: 
    - handle empty list 
    - 
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)

        while left < right: 
            mid = (left + right) // 2

            if self.canFinish(piles, mid, h): 
                right = mid
            else: 
                left = mid + 1
        return left

    def canFinish(self, piles, k, h): 
        hours = 0
        for pile in piles: 
            hours += (pile + k - 1) // k
        return hours <= h
        
