class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        COLS = set() 
        LEFT_TO_RIGHT_DIAG = set() # col + row is the same
        RIGHT_TO_LEFT_DIAG = set() # row - col is the same

        self.res = [] # [[ROW1_PLACEMENET, ROW2_PLACEMENT, ...]]
        self.backtrack(0, [], n, COLS, LEFT_TO_RIGHT_DIAG, RIGHT_TO_LEFT_DIAG)
        print(self.res)

        return self.construct_solution(n)


    def backtrack(self, curr_row, so_far, n, COLS, LEFT_TO_RIGHT_DIAG, RIGHT_TO_LEFT_DIAG):
        if len(so_far) == n:
            self.res.append(list(so_far))
            return 

        for j in range(n):
            if self.canPlace(curr_row, j, COLS, LEFT_TO_RIGHT_DIAG, RIGHT_TO_LEFT_DIAG):
                COLS.add(j)
                LEFT_TO_RIGHT_DIAG.add(j + curr_row)
                RIGHT_TO_LEFT_DIAG.add(curr_row - j)
                so_far.append(j)

                self.backtrack(curr_row + 1, so_far, n, COLS, LEFT_TO_RIGHT_DIAG, RIGHT_TO_LEFT_DIAG)

                so_far.pop()
                COLS.remove(j)
                LEFT_TO_RIGHT_DIAG.remove(j + curr_row)
                RIGHT_TO_LEFT_DIAG.remove(curr_row - j)


    def canPlace(
        self, 
        row, 
        col, 
        COLS,
        LEFT_TO_RIGHT_DIAG,
        RIGHT_TO_LEFT_DIAG
    ):
        if col in COLS or row - col in RIGHT_TO_LEFT_DIAG or row + col in LEFT_TO_RIGHT_DIAG:
            return False 
        
        return True 
    


    def construct_solution(self, n):
        res = [] 
        for solution in self.res:
            curr_solution = [] 
            for col in solution:
                QUEENS = ["."] * n
                QUEENS[col] = "Q"
                curr_solution.append("".join(QUEENS))
            
            res.append(curr_solution)
        
        return res
