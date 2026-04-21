class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        result = 0

        for right in range(len(s)):
            # 중복 발견 시 left를 당겨서 제거
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            result = max(result, right - left + 1)

        return result