class Node:
    def __init__(self):
        self.children = {} 
        self.isWord = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # form trie 
        root = Node() 

        for word in words:
            curr = root 
            
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node() 
                
                curr = curr.children[c]
            
            curr.isWord = word

        self.res = set()


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    self.dfs(i, j, set(), root, board)

        
        return [word for word in self.res]
    

    def dfs(self, row, col, seen, node, board):
        if (
            row < 0 or row >= len(board) or 
            col < 0 or col >= len(board[0]) or 
            (row, col) in seen or 
            board[row][col] not in node.children
        ):
            return 
        

        seen.add((row, col))

        # shift node to current letter 
        node = node.children[board[row][col]]

        # check if this is a word
        if node.isWord is not None:
            self.res.add(node.isWord)
        

        # check other sides 
        self.dfs(row + 1, col, seen, node, board)
        self.dfs(row - 1, col, seen, node, board)
        self.dfs(row, col + 1, seen, node, board)
        self.dfs(row, col - 1, seen, node, board)

        seen.remove((row, col))
