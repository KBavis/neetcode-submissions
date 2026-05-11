class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set() 
        num_islands = 0 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1" and (i, j) not in seen:
                    self.dfs(i, j, seen, grid)
                    num_islands += 1 
        

        return num_islands 
    

    def dfs(self, row, col, seen, grid):

        if (
            row >= len(grid) or 
            row < 0 or 
            col >= len(grid[0]) or 
            col < 0 or 
            (row, col) in seen or 
            grid[row][col] == "0"
        ):
            return 
        
        seen.add((row, col))

        self.dfs(row + 1, col, seen, grid)
        self.dfs(row - 1, col, seen, grid)
        self.dfs(row, col + 1, seen, grid)
        self.dfs(row, col - 1, seen, grid)        
