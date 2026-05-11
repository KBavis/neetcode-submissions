class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        # validate rows 
        ROWS = {i: set() for i in range(len(board))}

        # validate cols 
        COLS = {j: set() for j in range(len(board[0]))}

        # validate 3x3s 
        THREE_BY_THREES = {(i,j): set() for i in range(3) for j in range(3)}

        

        for i in range(len(board)):
            for j in range(len(board[0])):

                curr_val = board[i][j]
                if curr_val == ".":
                    continue 
                
                

                # check if curr_val is valid 
                if curr_val in ROWS[i] or curr_val in COLS[j] or curr_val in THREE_BY_THREES[(i // 3, j // 3)]:
                    return False 
                

                ROWS[i].add(curr_val)
                COLS[j].add(curr_val)
                THREE_BY_THREES[(i // 3, j // 3)].add(curr_val)
        

        return True 