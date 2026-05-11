class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        seen = set() 

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                area = self.dfs(i, j, seen, grid)
                max_area = max(area, max_area)
        

        return max_area
                

    
    def dfs(self, row, col, seen, grid):
        if (
            row >= len(grid) or 
            row < 0 or 
            col >= len(grid[0]) or 
            col < 0 or 
            (row, col) in seen or 
            grid[row][col] == 0
        ):
            return 0

        seen.add((row, col))

        area = 1
        
        area += self.dfs(row + 1, col, seen, grid)
        area += self.dfs(row - 1, col, seen, grid)
        area += self.dfs(row, col + 1, seen, grid)
        area += self.dfs(row, col - 1, seen, grid)

        return area

