class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
            Key Idea:
                - if a set of O's is connected to a particular edge, it CANNOT be flipped 
                - if we iterate through and find those O's that are connected to edge, then we know these are "safe" from being flipped 
        """



        def dfs(row, col):
            if (
                row < 0 or 
                col < 0 or 
                row >= len(board) or 
                col >= len(board[0]) or 
                board[row][col] != "O"
            ):
                return 
            

            # mark as safe 
            board[row][col] = "S"

            # search neighbors 
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        

        # check left and right edges 
        for i in range(len(board)):
            dfs(i, 0) 
            dfs(i, len(board[0]) - 1)
        

        # top and bottom edges 
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)
        

        # iterate through and perform flips 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
        

