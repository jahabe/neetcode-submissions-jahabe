class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # 1. create a stack list 
        stack = []
        # 2. for loop for each operation 
        for op in operations: 
            # 3. if operation[i] == "+" -> stack[-1] + stack[-2]
            if op == "+": 
                stack.append(stack[-1] + stack[-2])
            # 4. if operation[i] == "D" -> 2 * stack[-1]
            elif op == "D": 
                stack.append(stack[-1] * 2)
            # 5. if operation[i] == "C" -> pop
            elif op == "C": 
                stack.pop()
            # 6. if just integer -> int(op)
            else: 
                stack.append(int(op))
        #7. return sum of the stack
        return sum(stack)