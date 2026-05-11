class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS = len(board)
        COLS = len(board[0])


        def dfs(i, j):
            if (
                i < 0 or 
                i >= ROWS or 
                j < 0 or 
                j >= COLS or 
                board[i][j] != "O"
            ):
                return 
            

            # mark O as safe 
            board[i][j] = "S"

            # search surronding areas and do same 
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        

        # run DFS along each edge, marking relevant O's as safe from being flipped 
        for i in range(ROWS):
            dfs(i, 0) # left edge 
            dfs(i, COLS - 1) # right edge 
        

        for j in range(COLS):
            dfs(0, j) # top edge 
            dfs(ROWS - 1, j) # bottom edge 
        

        # flip those needing to be flipped 
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        

