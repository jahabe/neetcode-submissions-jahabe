# valid pairs: () {} []
# one way: remove matching pairs from string until nothing is left. 
# good sign: empty string means all pairs were matched. 
# bad sign: some characters remain in string means that string is invalid. 

# while the string contains () {} [], remove all occurences of those pairs 
# after that, if the string is empty -> return ture 
# otherwise, return false. 

class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s: 
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        
        return s == ''