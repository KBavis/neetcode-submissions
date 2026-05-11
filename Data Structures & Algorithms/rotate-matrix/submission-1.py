class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        self.transpose(matrix)
        self.swap(matrix)


    
    def transpose(self, matrix):

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        


    def swap(self, matrix):

        for i in range(len(matrix)):

            l = 0 
            r = len(matrix[i]) - 1 

            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1 
                r -= 1 
        