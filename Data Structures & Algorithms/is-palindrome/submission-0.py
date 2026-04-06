"""
Understand: 
    Given: string s
    Output: boolean type

    True: if it's a palindrome
    False: if it's not a palindrome 

    Constraints: 
    - Alphanumeric: (A-Z,a-z) and numbers (0-9)
    - case-insensitive and ignores all non-alphanumeric characters.

Plan: 
    new variable: newStr = ''
    check all the characters of string s --> for loop
    check for isalnum using if statement
    if it is alnum --> add c.lower() into newStr 
    return newStr == newStr[::-1]
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''

        for c in s: 
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]