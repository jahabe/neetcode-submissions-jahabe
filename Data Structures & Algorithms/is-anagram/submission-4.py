class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Understand: 
        - two strings -> s & t
        - same spells -> true | otherwise -> false
        - constraints: all lowercases

        Plan: 
        - we can try using if statements. 
        - edge case: not the same length -> return false
        - sort() and check ==

        Implement: 
        """
        if len(s) != len(t): 
            return False
        
        # return sorted(s) == sorted(t)

        #alternative way 1: Hash Map
        countS, countT = {}, {}
        for i in range(len(s)): 
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT
