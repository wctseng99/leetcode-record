class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(x, y):
            nonlocal curr_area
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            curr_area = 1
            curr_area += dfs(x+1, y)
            curr_area += dfs(x-1, y)
            curr_area += dfs(x, y+1)
            curr_area += dfs(x, y-1)

            return curr_area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_area = 0
                    max_area = max(max_area, dfs(i, j))

        return max_area