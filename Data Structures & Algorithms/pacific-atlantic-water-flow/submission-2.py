class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        COLS = len(heights[0])
        ROWS = len(heights)


        def dfs(row, col, visited, prev):
            if (row, col) in visited or row >= ROWS or row < 0 or col >= COLS or col < 0 or prev > heights[row][col]:
                return 
            
            visited.add((row, col))
            
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
        

        atl, pac = set(), set()

        for i in range(ROWS):
            dfs(i, COLS - 1, atl, float('-inf'))
            dfs(i, 0, pac, float('-inf'))
        
        for j in range(COLS):
            dfs(0, j, pac, float('-inf'))
            dfs(ROWS - 1, j, atl, float('-inf'))
        
        result = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in atl and (i,j) in pac:
                    result.append([i,j])
        
        return result
