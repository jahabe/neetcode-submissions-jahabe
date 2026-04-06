"""

"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        #1. one string variable 만들기
        res = ""
        for s in strs: 
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        #list result and pointer i
        res, i = [], 0

        #while string is in boundary
        while i < len(s): 
            #second pointer j
            j = i
            while s[j] != '#': 
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length]) #entire string 
            i = j + 1 + length
        return res