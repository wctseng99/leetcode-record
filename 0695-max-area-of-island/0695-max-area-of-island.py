class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            curr_area = 1
            curr_area += dfs(x+1, y) + dfs(x-1, y) + dfs(x, y+1) + dfs(x, y-1)

            return curr_area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    current_area = dfs(i, j)
                    max_area = max(max_area, current_area)

        return max_area