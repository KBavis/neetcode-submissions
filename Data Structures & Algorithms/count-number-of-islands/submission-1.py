class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        numIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in seen:
                    self.search(i, j, seen, grid)
                    numIslands += 1
                

        return numIslands

    def search(self, row, col, seen, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in seen or grid[row][col] == "0":
            return 
        
        seen.add((row, col))

        self.search(row + 1, col, seen, grid)
        self.search(row - 1, col, seen, grid)
        self.search(row, col + 1, seen, grid)
        self.search(row, col - 1, seen, grid)