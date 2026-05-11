class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        self.res = [] 
        self.n = n

        self.backtrack(0, [], set(), set(), set(), set())

        return self.res


    
    def construct_solution(self, queen_positions):
        formatted = [] 

        for row, col in queen_positions:

            temp = ['.' for i in range(self.n)]
            temp[col] = "Q"
            formatted.append(''.join(temp))

        return formatted





    def backtrack(self, row_idx, soFar, rows, cols, left_diag, right_diag):
            
        if len(soFar) == self.n:
            self.res.append(
                self.construct_solution(list(soFar))
            )
            return 
            

        for row in range(row_idx, self.n):
            for col in range(self.n):

                if self.can_place(row, col, rows, cols, left_diag, right_diag):

                    rows.add(row)
                    cols.add(col)
                    left_diag.add(row + col)
                    right_diag.add(col - row)

                    soFar.append((row,col))

                    self.backtrack(row + 1, soFar, rows, cols, left_diag, right_diag)

                    soFar.pop()

                    rows.remove(row)
                    cols.remove(col)
                    left_diag.remove(row + col)
                    right_diag.remove(col - row)


    def can_place(self, row, col, rows, cols, left_diag, right_diag):
            
        return (
            row not in rows and 
            col not in cols and 
            row + col not in left_diag and 
            col - row not in right_diag 
        )

                
        


