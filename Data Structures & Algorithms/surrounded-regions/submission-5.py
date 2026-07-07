class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
            1. Itereate through entire board
            2. When we see a location that's an O, called "isSurroudned"
            3. Is surrounded will transverse in all directions. 
            4. Returns back true or false (if true, add locations tracked in set to entire set)
            5. Iterate throug hset and change in palce 
        """

        surrounded_locations = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == "O" and (i,j) not in surrounded_locations:    
                    curr_set = set()
                    if self.is_surrounded(i, j, board, curr_set):
                        print(f"Found surroudned locations from search({i},{j}), locations={curr_set}")
                        surrounded_locations.update(curr_set)
        


        for i, j in surrounded_locations:
            board[i][j] = "X"
    


    def is_surrounded(self, row, col, board, seen):
        if (
            row < 0 or 
            col < 0 or 
            row >= len(board) or 
            col >= len(board[0])
        ):
            return False
        elif board[row][col] == "X" or (row, col) in seen:
            return True 
        

        # current value is an O
        seen.add((row, col))

        # in order for this to be surrounded, all sides must have an X 
        if (
            self.is_surrounded(row + 1, col, board, seen) and 
            self.is_surrounded(row - 1, col, board, seen) and 
            self.is_surrounded(row, col + 1, board, seen) and 
            self.is_surrounded(row, col - 1, board, seen)
        ):
            return True 
        

        return False 
        

