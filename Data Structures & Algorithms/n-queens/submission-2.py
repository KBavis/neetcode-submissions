class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Goal:
            - attempt to find locations on each row where we can place queen 
            - we need to track ideas such as "can we place on this row, column, left diag, right diag" 


        Column:
            - set 
        
        Row: 
            - set 
        
        Left Diag: 
            - (0,0), (1,1), (2,2) --> 0
            - (1,0), (2,1) --> 1
            - (0,2), (1, 3) --> 2 
            --> utilzie the difference between the row and column as unique identifer 
        
        Right Diag: 
            - (2,0), (1,1), (0,2) --> add to two 
            - (3,0), (2,1), (1,2), (0 ,3) --> add for unique identifeir 
        """

        self.positions = [] 
        self.backtrack(0, n, [], set(), set(), set())
        return self.construct_result(self.positions, n)
    

    def backtrack(self, row, n, soFar, cols, left_to_right, right_to_left):
        if len(soFar) == n:
            self.positions.append(list(soFar))
            return 
        
        
        for j in range(n):
                
            # check if we can place the queen
            if self.can_place(row, j, cols, left_to_right, right_to_left):


                cols.add(j)
                left_to_right.add(row - j)
                right_to_left.add(row + j)
                soFar.append((row, j))


                self.backtrack(row + 1, n, soFar, cols, left_to_right, right_to_left)

                cols.remove(j)
                left_to_right.remove(row -j)
                right_to_left.remove(row + j)
                soFar.pop() 

    """
        cols = 1, 3 
        left_to_right = (1, 2)
        right_to_left = (1, 4)
    """

    def construct_result(self, positions, n):
        final = [] 
        print(positions)

        for res in positions:
            curr = []

            for pos in res:
                dots = ["."] * n
                dots[pos[1]] = "Q"
                curr.append("".join(dots))
            
            final.append(curr)
        
        print(final)

        
        return final



    def can_place(self, curr_row, curr_col, cols, left_to_right, right_to_left):
        return (
            curr_col not in cols and 
            curr_row - curr_col not in left_to_right and 
            curr_row + curr_col not in right_to_left
        )


