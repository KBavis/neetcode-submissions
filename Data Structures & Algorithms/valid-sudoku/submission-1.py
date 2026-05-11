class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # validate values in 3x3 block are 1-9 (no duplicates)

        # validate values in each row are 1-9 (no duplicates)

        # validate values in each col are 1-9 (no duplicates)

        

        """
            1) We need a map from the row to its respective values
                    a) <row1>: set() --> store all row1 values  {0: set()}
                    b) see a duplicate value in row1, return False 
            
            2) We need a map from the col to its respective values 
                    a) <col1> : set() --> store all col1 values {1: set()}
                    b) see duplicate, return False

            3) Once we have spanned 3 rows of values (and not run into any duplicates on columns or rows), we need to validate the three
                3x3 matrices 

                for i in range(len(board)):
                    for j in range(len(board[0])):        
        """


        COLS = {j: set() for j in range(len(board[0]))} 
        ROWS = {i: set() for i in range(len(board))} 
        THREE_BY_THREE = {(i,j): set() for i in range(3) for j in range(3)}



        for i in range(len(board)):
            for j in range(len(board[0])):

                curr_val = board[i][j]
                if curr_val == ".":
                    continue 
                
                if curr_val in COLS[j] or curr_val in ROWS[i] or curr_val in THREE_BY_THREE[(i // 3, j // 3)]:
                    return False 
                
                COLS[j].add(curr_val)
                ROWS[i].add(curr_val)
                THREE_BY_THREE[(i // 3, j // 3)].add(curr_val)
        
        return True 
                


