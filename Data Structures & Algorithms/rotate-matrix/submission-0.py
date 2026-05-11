class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        def transpose(matrix):

            for i in range(len(matrix)):
                for j in range(i):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp 
        

        def swap(matrix):

            for i in range(len(matrix)):

                left = 0 
                right = len(matrix[i]) - 1 

                while left < right:
                    temp = matrix[i][left]
                    matrix[i][left] = matrix[i][right]
                    matrix[i][right] = temp 

                    left += 1 
                    right -= 1 
        
        transpose(matrix)
        swap(matrix)