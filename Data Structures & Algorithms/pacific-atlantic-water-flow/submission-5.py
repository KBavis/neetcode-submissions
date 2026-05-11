class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
            - flow in any direction as long as the cell is <= current height 
            - start at each "borders", and goes as far as possible 
            - for any cell where the two overlap, this is in our anser
        """


        ATL = set() 
        PAC = set() 
        


        def dfs(row, col, seen, prevHeight):
            if (
                row >= len(heights) or col >= len(heights[0]) or 
                row < 0 or col < 0 or 
                (row, col) in seen
                or prevHeight > heights[row][col]
            ):
                return 
            

            seen.add((row, col))
            prevHeight = heights[row][col]

            dfs(row + 1, col, seen, prevHeight)
            dfs(row - 1, col, seen, prevHeight)
            dfs(row, col + 1, seen, prevHeight)
            dfs(row, col - 1, seen, prevHeight)
        


        
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, ATL, float('-inf'))
            dfs(i, 0, PAC, float('-inf'))

        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, ATL, float('-inf'))
            dfs(0, j, PAC, float('-inf'))
        

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in ATL and (i,j) in PAC:
                    res.append([i,j])
        
        return res 