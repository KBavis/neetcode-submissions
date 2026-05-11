class Solution:
    class Node:
        def __init__(self):
            self.children = {} 
            self.word = None

    class Trie:
        def __init__(self):
            self.root = Solution.Node() 
        
        def add(self, word):
            curr = self.root 

            for c in word:
                if c not in curr.children:
                    curr.children[c] = Solution.Node() 
                
                curr = curr.children[c]
            
            curr.word = word


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result = set()

        # add to Trie 
        trie = self.Trie()
        for word in words:
            trie.add(word)
        
        root = trie.root 
        result = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                # start of a word
                c = board[i][j]
                if c in root.children:
                    self.backtrack(board, i, j, set(), root)
        
        return list(self.result)
    

    def backtrack(self, board, row, col, seen, node):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or (row,col) in seen or board[row][col] not in node.children:
            return False 
        

        seen.add((row, col))
        c = board[row][col]
        node = node.children[c]

        if node.word:
            self.result.add(node.word)


        self.backtrack(board, row - 1, col, seen, node)
        self.backtrack(board, row + 1, col, seen, node)
        self.backtrack(board, row, col - 1, seen, node)
        self.backtrack(board, row, col + 1, seen, node) 
 
        

        seen.remove((row,col))

        return False 



        