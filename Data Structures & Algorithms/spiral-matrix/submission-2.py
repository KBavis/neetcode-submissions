class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = [] 

        left, right = 0, len(matrix[0]) - 1 
        top, bottom = 0, len(matrix) - 1

        """
            top = 0 , bottom = 2 
            left = 0, right = 2 

            top = 1, bottom = 1, left = 1, right = 1 

            top = 2, bottom = 1, left = 1, right = 0
        """


        while left <= right and top <= bottom: 

            # left to right first 
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1 

            # top to bottom 
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -=  1 


            # right to left 
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1 
            
            # bottom to top 
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1 
        
        return res 