class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        COLS = len(heights[0])
        ROWS = len(heights)
        pacific, atlantic = set(), set() 

        def dfs(row, col, visited, prevHeight):
            if (row, col) in visited or \
                row < 0 or col < 0 or \
                row == ROWS or col == COLS or \
                prevHeight > heights[row][col]:
                    return 
            
            visited.add((row, col))

            dfs(row - 1, col, visited, heights[row][col])
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])



        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, COLS - 1, atlantic, heights[row][COLS - 1])
        
        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col])
            dfs(ROWS - 1, col, atlantic, heights[ROWS - 1][col])
        

        result = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in atlantic and (row, col) in pacific:
                    result.append([row, col])
        

        return result 
                




        



