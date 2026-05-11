class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # O(m * n) time 
        # O(m + n) 
        
        cols = {
            i: set() for i in range(len(board[0]))
        }

        rows = {
            i: set() for i in range(len(board))
        }

        three_by_three = {
            (i,j): set() for i in range(3) for j in range(3)
        }

        for i in range(len(board)):
            for j in range(len(board[0])):

                curr = board[i][j]
                if curr == ".":
                    continue 

                if (
                    curr in cols[j] or 
                    curr in rows[i] or 
                    curr in three_by_three[(i // 3, j // 3)] 
                ):
                    return False 
                

                cols[j].add(curr)
                rows[i].add(curr)
                three_by_three[(i // 3, j // 3)].add(curr)
        

        return True 
