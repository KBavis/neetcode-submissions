class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False 
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.search(i, j, board, word, set(), 0):
                    return True 
        

        return False 
    

    def search(self, i, j, board, word, seen, idx):
        if idx == len(word):
            return True
        elif (
            i >= len(board) or 
            j >= len(board[i]) or 
            i < 0 or 
            j < 0 or 
            (i,j) in seen or
            board[i][j] != word[idx] 
        ):
            return False 
        

        seen.add((i,j))

        if (
            self.search(i + 1, j, board, word, seen, idx + 1) or 
            self.search(i - 1, j, board, word, seen, idx + 1) or 
            self.search(i, j - 1, board, word, seen, idx + 1) or 
            self.search(i, j + 1, board, word, seen, idx + 1) 
        ):
            return True 
        
        seen.remove((i,j))