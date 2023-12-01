class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        
        # travere from top left to bottom right
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    # check if the upper side is land
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    # check if the left side is land
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        
        return perimeter