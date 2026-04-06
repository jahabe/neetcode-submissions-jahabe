class Solution:
    def trap(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        leftMax = heights[l]
        rightMax = heights[r]

        res = 0

        while l < r: 
            if leftMax < rightMax: 
                l += 1
                leftMax = max(leftMax, heights[l])
                res += leftMax - heights[l]
            else: 
                r -= 1
                rightMax = max(rightMax, heights[r])
                res += rightMax - heights[r]

        return res