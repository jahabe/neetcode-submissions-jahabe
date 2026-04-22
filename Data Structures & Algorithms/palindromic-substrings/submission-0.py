class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left, right):
            nonlocal count
            # 범위 안에 있고 양쪽 글자가 같으면 계속 확장
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1       # 팰린드롬 발견할때마다 카운트!
                left -= 1
                right += 1

        for i in range(len(s)):
            # 홀수 길이 (중심 1개, 예: "aba")
            expand(i, i)
            # 짝수 길이 (중심 2개, 예: "aa")
            expand(i, i + 1)

        return count