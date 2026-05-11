class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low_row = 0 
        high_row = len(matrix) - 1 

        low_col = 0 
        high_col = len(matrix[0]) - 1 


        while low_row <= high_row:

            mid_row = (low_row + high_row) // 2 
            
            # check if row would contain value 
            curr_low_row = matrix[mid_row][low_col]
            curr_high_row = matrix[mid_row][high_col]

            if target >= curr_low_row and target <= curr_high_row:
                # we found the target row !     
                while low_col <= high_col:

                    mid_col = (low_col + high_col) // 2 
                    if matrix[mid_row][mid_col] == target:
                        return True # found target value !
                    elif target < matrix[mid_row][mid_col]:
                        high_col = mid_col - 1 
                    else:
                        low_col = mid_col + 1 
                
                return False # found target row, but wasn't present in any of the columns 

            elif target < curr_low_row:
                # current row contains values greater than target value 
                high_row = mid_row - 1 
            else:
                # current row contains values less than target value 
                low_row = mid_row + 1 
        

        return False 
