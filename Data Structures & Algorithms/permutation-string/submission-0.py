class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)

        if m > n: return False 

        a = ord('a')
        c1 = [0]*26
        c2 = [0]*26
        
        for i in range(m): 
            c1[ord(s1[i]) - a] += 1
            c2[ord(s2[i]) - a] += 1
        
        if c1 == c2: return True 

        for r in range(m,n):
            c2[ord(s2[r]) - a] += 1
            c2[ord(s2[r-m]) - a] -= 1
            if c1 == c2: return True 
        return False