class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(x, y, index):
            if index == len(word):
                return True
            elif 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[index]:
                temp, board[x][y] = board[x][y], "X"
                is_find = dfs(x+1, y, index+1) or dfs(x-1, y, index+1) or dfs(x, y+1, index+1) or dfs(x, y-1, index+1)
                board[x][y] = temp
            else:
                return False
            return is_find

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                    
        return False