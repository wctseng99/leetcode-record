class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i: int, j: int, n: int) -> bool:
            if n == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[n]:
                return False
            else:
                temp, board[i][j] = board[i][j], -1 
                next = dfs(i+1, j, n+1) or dfs(i-1, j, n+1) or dfs(i, j+1, n+1) or dfs(i, j-1, n+1)
                board[i][j] = temp
                return next

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
                    