class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = {j: set() for j in range(len(board[0]))}
        rows = {i: set() for i in range(len(board))}
        three_by_threes = {(i,j): set() for i in range(3) for j in range(3)}

        for i in range(len(board)):

            for j in range(len(board[i])):
                curr = board[i][j]

                #skip empty values 
                if not curr or curr == ".":
                    continue

                # check if this value has been set before in corresponding cols/rows
                if curr in cols[j] or curr in rows[i] or curr in three_by_threes[(i // 3, j // 3)]:
                    return False 
                
                # add to both if not already there 
                cols[j].add(curr)
                rows[i].add(curr)
                three_by_threes[(i // 3, j // 3)].add(curr)


        return True 






