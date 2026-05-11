class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac = set()
        atl = set()  

        def search(i, j, prevHeight, visited):
            if (
                i < 0 or 
                i >= len(heights) or 
                j < 0 or 
                j >= len(heights[0]) or 
                (i,j) in visited or
                prevHeight > heights[i][j] 
            ):
                return 

            
            visited.add((i, j))

            search(i, j + 1, heights[i][j], visited)
            search(i, j - 1, heights[i][j], visited)
            search(i + 1, j, heights[i][j], visited)
            search(i - 1, j, heights[i][j], visited)

        



        # search from each boundary 
        for i in range(len(heights)):
            search(i, 0, float('-inf'), pac)
            search(i, len(heights[0]) - 1, float('-inf'), atl)
        

        for j in range(len(heights[0])):
            search(0, j, float('-inf'), pac)
            search(len(heights) - 1, j, float('-inf'), atl)
        

        # find intersection 
        res = []
        for i in range(len(heights)): 
            for j in range(len(heights[0])):

                if (i, j) in atl and (i,j) in pac:
                    res.append([i,j])
        

        return res
        




