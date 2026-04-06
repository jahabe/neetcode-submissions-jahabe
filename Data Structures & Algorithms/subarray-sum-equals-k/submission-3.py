class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = {0: 1}   # prefix sum 0 seen once

        for num in nums:
            prefix += num

            if prefix - k in seen:
                count += seen[prefix - k]

            seen[prefix] = seen.get(prefix, 0) + 1

        return count