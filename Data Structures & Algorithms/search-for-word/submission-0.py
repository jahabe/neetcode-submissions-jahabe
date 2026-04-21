class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set() 

        def dfs(row, col, index): 
            if index == len(word): 
                return True
            if row < 0 or col < 0 or row >= rows or col >= cols: 
                return False 
            if board[row][col] != word[index]: 
                return False 
            if (row, col) in visited: 
                return False 
            
            visited.add((row, col))

            found = (dfs(row + 1, col, index + 1) or 
                     dfs(row - 1, col, index + 1) or 
                     dfs(row, col + 1, index + 1) or 
                     dfs(row, col - 1, index + 1))
            
            visited.remove((row, col))
            return found 
        
        for r in range(rows): 
            for c in range(cols): 
                if dfs(r, c, 0): 
                    return True 
        return False