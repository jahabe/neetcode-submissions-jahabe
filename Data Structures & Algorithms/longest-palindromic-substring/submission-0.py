class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            odd = expand(i, i)        # 홀수: "bab"
            even = expand(i, i + 1)   # 짝수: "bb"

            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even

        return result