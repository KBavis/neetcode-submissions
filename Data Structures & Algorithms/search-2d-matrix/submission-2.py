class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        # find row 
        low = 0 
        high = len(matrix) - 1
        row = self.search_row(matrix, target, low, high)
        if row is None:
            return False 

        # find col 
        low = 0 
        high = len(matrix[0]) - 1
        col = self.search_col(matrix, target, row, low, high)
        if col is None:
            return False 
        
        return True 

    
    def search_col(self, matrix, target, row, low, high):

        while low <= high:

            mid = (low + high) // 2

            if matrix[row][mid] == target:
                return mid 
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1 
        
        return None

    def search_row(self, matrix, target, low, high):

        while low <= high:

            mid = (low + high) // 2


            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[0]) - 1]:
                return mid 
            elif target < matrix[mid][0]:
                high = mid - 1 
            else:
                low = mid + 1

        return None
