class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque([])
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = 0
                    queue.append((i, j))
                    self.adjacent_lands(queue, grid)
                    island += 1
        return island

    def adjacent_lands(self, queue, grid):   
        while queue:
            i, j = queue.popleft()
            for row, col in (i+1, j), (i-1, j), (i, j+1), (i, j-1):         
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1":
                    queue.append((row, col))
                    grid[row][col] = 0
