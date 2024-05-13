class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, i):
            if x < 0 or x > len(board) - 1  or y < 0 or y > len(board[0]) -1  or board[x][y] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            
            temp = board[x][y]
            board[x][y] = "x"
            result = dfs(x-1, y, i+1) or dfs(x+1, y, i+1) or dfs(x, y-1, i+1) or dfs(x, y+1, i+1) 
            board[x][y] = temp
            return result
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False