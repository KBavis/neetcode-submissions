class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        if not matrix:
            return

        isFirstRowZero = False 
        isFirstColZero = False 

        # check if the first col contains a zero
        for i in range(len(matrix)): 
            if matrix[i][0] == 0:
                isFirstColZero = True 
                break 
        
        # check if the first row contains a zero
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                isFirstRowZero = True 
                break 


        # find & store indicator if zero in respective col/row in first col/row 
        for i in range(1, len(matrix), 1):
            for j in range(1, len(matrix[0]), 1):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0 
        

        # iterate through and update values to be zero if necessary 
        for i in range(1, len(matrix), 1):
            for j in range(1, len(matrix[0]), 1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        

        # update first row 
        if isFirstRowZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        

        # update first col 
        if isFirstColZero: 
            for i in range(len(matrix)):
                matrix[i][0] = 0 



        