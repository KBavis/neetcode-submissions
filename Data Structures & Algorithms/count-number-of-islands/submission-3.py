class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.ROWS = len(grid)
        self.COLS = len(grid[0])

        seen = set()
        total_islands = 0
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if (i, j) not in seen and grid[i][j] == "1":
                    self.dfs(i, j, grid, seen)
                    total_islands += 1 
        

        return total_islands
    

    def dfs(self, row, col, grid, seen):
        if (
            row < 0 or 
            col < 0 or 
            row >= self.ROWS or 
            col >= self.COLS or 
            (row, col) in seen or 
            grid[row][col] != "1"
        ):
            return 
        

        seen.add((row, col))

        self.dfs(row + 1, col, grid, seen)
        self.dfs(row - 1, col, grid, seen)
        self.dfs(row, col + 1, grid, seen)
        self.dfs(row, col - 1, grid, seen)

