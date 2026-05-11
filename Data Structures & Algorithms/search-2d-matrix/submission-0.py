class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        """
            1. If target > matrix[currRow]
        """

        row_low = 0 
        row_high = len(matrix) - 1
        col_low = 0
        col_high = len(matrix[0]) - 1

        while row_low <= row_high:

            mid_row = (row_low + row_high) // 2 
            
            # we found the row
            if matrix[mid_row][col_low] <= target and matrix[mid_row][col_high] >= target:
                return self.searchCols(mid_row, col_low, col_high, matrix, target)
            elif matrix[mid_row][0] > target:
                row_high = mid_row - 1 
            else:
                row_low = mid_row + 1
        

        return False
    

    def searchCols(self, row, low, high, matrix, target):

        while low <= high:
            
            mid = (low + high) // 2

            if matrix[row][mid] == target:
                return True 
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1 
        
        return False 