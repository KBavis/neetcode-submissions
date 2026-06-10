class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        def dfs(row, col, prev_height, seen):
            if (
                row >= len(heights) or 
                col >= len(heights[0]) or 
                col < 0 or 
                row < 0 or 
                (row, col) in seen or 
                heights[row][col] < prev_height
            ):
                return 
            

            seen.add((row, col))

            # check other directions 
            dfs(row + 1, col, heights[row][col], seen)
            dfs(row - 1, col, heights[row][col], seen)
            dfs(row, col - 1, heights[row][col], seen)
            dfs(row, col + 1, heights[row][col], seen)

        

        # locations where water can flow 
        ATL = set()
        PAC = set() 


        # rows 
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, float('-inf'), ATL)
            dfs(i, 0, float('-inf'), PAC)
        
        # cols 
        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, float('-inf'), ATL)
            dfs(0, j, float('-inf'), PAC)
        
        # determine which cells water overlapped 
        res = [] 
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in ATL and (i,j) in PAC:
                    res.append([i,j])
        

        return res

