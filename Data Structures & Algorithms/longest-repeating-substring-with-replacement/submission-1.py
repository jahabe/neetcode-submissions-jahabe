class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            # 교체 필요 횟수가 k 초과하면 window 줄이기
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result