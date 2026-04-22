class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0  # 2칸 전
        prev1 = 0  # 1칸 전

        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1