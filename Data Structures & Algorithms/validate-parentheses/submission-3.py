# valid parethesis must follow Last-opened and first closed order. () {} []
# whenver we see a closing bracket, we check the stack for the most recent opening bracket. 
# if it matches -> we can remove the opening bracket from the stack. 
# if it doesn't or the stack is empty -> the string is invalid. 
# True case is the same as string ends with an empty stack. 

# let's create a stack to store opening brackets. 
# for each character in the string: 
# if we see the opening bracket, push it onto the stack. 
# if we see the closing bracket, check the stack for emptiness first, then top matches. 
# if matches, pop the stack, if not, return false. 
# after that, if the stack is empty, good! True 
#if not, return False. 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for c in s: 
            if c in closeToOpen: 
                if stack and stack[-1] == closeToOpen[c]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(c)
        
        return True if not stack else False