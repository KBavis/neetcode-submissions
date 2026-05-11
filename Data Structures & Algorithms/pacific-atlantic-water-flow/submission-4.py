class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        
    
        def dfs(i, j, visited, prevHeight):
            if (
                i >= ROWS or 
                i < 0 or 
                j >= COLS or 
                j < 0 or 
                prevHeight > heights[i][j] or 
                (i, j) in visited
            ):
                return 
            
            visited.add((i, j))


            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i + 1, j, visited, heights[i][j])

        atl = set() 
        pac = set()
        

        for i in range(ROWS):
            dfs(i, 0, pac, float('-inf'))
            dfs(i, COLS - 1, atl, float('-inf'))
        
        for j in range(COLS):
            dfs(0, j, pac, float('-inf'))
            dfs(ROWS - 1, j, atl, float('-inf'))
        

        res= [] 

        for i in range(ROWS):
            for j in range(COLS):

                if (i, j) in atl and (i, j) in pac:
                    res.append([i,j])
        

        return res