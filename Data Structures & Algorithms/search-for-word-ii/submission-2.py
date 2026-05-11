class Node:
    def __init__(self):
        self.children = {} 
        self.isWord = False 
    
    def insert_word(self, word: str):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            
            curr = curr.children[c]
        
        curr.isWord = True 
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        if not words or not board:
            return []
        
        self.result = []
        
        root = Node()
        for word in words: 
            root.insert_word(word)
        

        for row in range(len(board)):
            for col in range(len(board[0])):
                self.search(row, col, set(), [], board, root)
        

        return self.result 
    

    def search(self, row, col, seen, soFar, board, node):
        if (row < 0 or row >= len(board) or 
                col < 0 or col >= len(board[0]) or 
                board[row][col] not in node.children or  
                (row, col) in seen):
                return 

        c = board[row][col]

        soFar.append(c)
        seen.add((row, col))

        node = node.children[c]
        if node.isWord:
            word = "".join(soFar)
            self.result.append(word)
            node.isWord = False
        

        self.search(row + 1, col, seen, soFar, board, node)
        self.search(row - 1, col, seen, soFar, board, node)
        self.search(row, col - 1, seen, soFar, board, node)
        self.search(row, col + 1, seen, soFar, board, node)

        soFar.pop()
        seen.remove((row,col))
