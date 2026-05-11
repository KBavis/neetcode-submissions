class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low_row = 0 
        high_row = len(matrix) - 1 

        low_col = 0 
        high_col = len(matrix[0]) - 1

        while low_row <= high_row: 

            mid_row = (high_row + low_row) // 2 

            # check if this row contains our target element
            if target >= matrix[mid_row][low_col] and target <= matrix[mid_row][high_col]:

                # search for element in current row (if not found, return false)
                while low_col <= high_col:
                    mid_col = (high_col + low_col) // 2 

                    if matrix[mid_row][mid_col] == target:
                        return True 
                    elif matrix[mid_row][mid_col] > target:
                        high_col = mid_col - 1 
                    else:
                        low_col = mid_col + 1 
                
                # if we expected to find value in this row and its not present, terminate early
                return False
            elif target > matrix[mid_row][high_col]:
                low_row = mid_row + 1
            else:
                high_row = mid_row - 1 
        

        return False 