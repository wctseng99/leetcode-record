class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([tuple(entrance)])
        step = 0
        visited = set()
        visited.add(tuple(entrance))

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                # check if the cell a exist
                if i == 0 or j == 0 or i == len(maze) - 1 or  j == len(maze[0]) - 1:
                    if maze[i][j] == '.' and [i, j] != entrance:
                        return step
                # bfs
                for row, col in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == "." and (row, col) not in visited:
                        visited.add((row, col))
                        queue.append((row, col))
                
            step += 1
        return -1