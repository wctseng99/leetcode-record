class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh_oranges = minute = 0
        queue = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, minute))
        
        while queue:
            i, j, minute = queue.popleft()
            for row, col in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                    fresh_oranges -= 1
                    grid[row][col] = 2
                    queue.append((row, col, minute+1))

        return -1 if fresh_oranges else minute
