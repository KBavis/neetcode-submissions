class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if self.backtrack(board, i, j, 0, set(), word):
                        return True 
        
        return False 
    

    def backtrack(self, board, row, col, index, seen, word):
        if index == len(word):
            return True 
        elif row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in seen or board[row][col] != word[index]:
            return False 
        

        seen.add((row,col))

        if self.backtrack(board, row + 1, col, index + 1, seen, word) or \
            self.backtrack(board, row - 1, col, index + 1, seen, word) or \
            self.backtrack(board, row, col + 1, index + 1, seen, word) or \
            self.backtrack(board, row, col - 1, index + 1, seen, word):

            return True 
        

        seen.remove((row, col))
        return False 
