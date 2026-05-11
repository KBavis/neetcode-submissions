class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set() 
        total = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in seen and grid[i][j] == '1':
                    self.search(i,j,seen,grid)
                    total += 1
        
        return total 
    
    def search(self, i, j, seen, grid):
        if i < 0 or j < 0 or \
            i >= len(grid) or j >= len(grid[0]) or \
            (i,j) in seen or \
            grid[i][j] != '1':
                return 
        
        seen.add((i,j))

        self.search(i + 1, j, seen, grid)
        self.search(i - 1, j, seen, grid)
        self.search(i, j + 1, seen, grid)
        self.search(i, j - 1, seen, grid)
        