class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
            - iterate through --> O(n * m)
            - check if the current location is a 1 
            - if it is a 1, we perform dfs (checking left, right, up, down) for more ones 
            - keeping track of ones we've seen in a set 
            - return 1 + X where the base case is 0 
        """

        visited = set()
        max_area = 0 

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1 and (i,j) not in visited:
                    curr_area = self.dfs(i, j, grid, visited)
                    max_area = max(max_area, curr_area)
        

        return max_area 
    

    def dfs(self, row, col, grid, seen):
        if (
            row < 0 or 
            col < 0 or 
            row >= len(grid) or 
            col >= len(grid[0]) or 
            (row, col) in seen or 
            grid[row][col] == 0
        ):
            return 0 
        
        # found a one !
        seen.add((row, col))
        total = 1

        total += self.dfs(row + 1, col, grid, seen)
        total += self.dfs(row - 1, col, grid, seen)
        total += self.dfs(row, col - 1, grid, seen)
        total += self.dfs(row, col + 1, grid, seen)

        return total 
                
        