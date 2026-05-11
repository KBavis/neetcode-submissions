class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        """
            iterate through the array one time to find cols and rows that have 0's 
            store these in a set 
            re-itrate through and zero out the vlaue if its in one of sets 

            o n * m space 

            if matrix[i][j] == 0 
                --> matrix[i][0] = 0 
                --> matrix[j][0] = 0 
            
            need to first check if the 0th row and 0th column have zeros and then apply after processing (or else we run into issues)
        """ 

        # check if first row / col have zeros 
        first_row_zero = False
        first_col_zero = False 

        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                first_col_zero = True 
                break 
        
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                first_row_zero = True 
                break 
        

        # find cols/rows with zero 
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 
                    matrix[0][j] = 0 
        

        # zero out columns/rows if needed 
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 
        

        # account for first col / row zeroing out as well;
        if first_row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0 
        
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0 
                
