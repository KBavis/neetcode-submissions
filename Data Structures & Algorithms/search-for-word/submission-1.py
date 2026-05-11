class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if self.backtrack(board, word, i, j, 0, set()):
                        return True 
        
        return False 
    

    def backtrack(self, board, word, row, col, idx, seen):
        if len(word) == idx:
            return True
        
        if row >= len(board) or col >= len(board[0]) or col < 0 or row < 0 or (row, col) in seen or board[row][col] != word[idx]:
            return False
         
        
       
        seen.add((row,col))

        if (
            self.backtrack(board, word, row, col + 1, idx + 1, seen) or
            self.backtrack(board, word, row, col - 1, idx + 1, seen) or 
            self.backtrack(board, word, row - 1, col, idx + 1, seen) or 
            self.backtrack(board, word, row + 1, col, idx + 1, seen)
        ):
            return True
                    
        seen.remove((row,col))
        return False 
