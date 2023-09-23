class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
    
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"

        while queue:
            i, j, step = queue.popleft()
            for row, col in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == ".":
                    if row == 0 or col ==0 or row == len(maze) -1 or col == len(maze[0]) - 1:
                        return step + 1
                    maze[row][col] = "+"
                    queue.append((row, col, step+1))
        return -1