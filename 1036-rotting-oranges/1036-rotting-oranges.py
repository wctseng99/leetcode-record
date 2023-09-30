class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        fresh_oranges = minute = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, minute))
                if grid[i][j] == 1:
                    fresh_oranges += 1

        while queue:
            i, j, minute = queue.popleft()
            for row, col in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                    grid[row][col] = 2
                    fresh_oranges -= 1
                    queue.append((row, col, minute+1)) 

        return -1 if fresh_oranges else minute