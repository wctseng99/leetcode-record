class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(x, y):
            if x < 0 or x >= len(grid1) or y < 0 or y >= len(grid1[0]) or grid2[x][y] == 0:
                return 
            grid2[x][y] = 0
            for row, col in [x+1, y], [x-1, y], [x, y+1], [x, y-1]:
                dfs(row, col)

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(i, j)
        
        sub_islands = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    sub_islands += 1
                    dfs(i, j)

        return sub_islands