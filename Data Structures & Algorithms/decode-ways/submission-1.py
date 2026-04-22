"""
"12" → "AB" (1,2) 또는 "L" (12) → 2가지
"01" → 0으로 시작하면 무조건 invalid → 0가지

핵심 아이디어
Climb Stairs랑 똑같은 구조!
매 숫자마다 두가지 선택:
    1. 한자리로 읽기  (1~9)
    2. 두자리로 읽기  (10~26)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        prev2 = 1
        prev1 = 1 if s[0] != '0' else 0 

        for i in range(1, len(s)): 
            current = 0

            # 한자리로 읽기 (0이면 안됨)
            if s[i] != '0': 
                current += prev1
            
            # 두자리로 읽기
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26: 
                current += prev2 
            
            prev2 = prev1 
            prev1 = current
        return prev1