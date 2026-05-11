class Node:

    def __init__(self):
        self.children = {} # set of letters that are children of this current node 
        self.word = None # set this to the actual word formed if its a word 

class Trie:

    def __init__(self):
        self.root = Node() 
    

    def insert(self, word):
        curr = self.root 

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node() 
            
            curr = curr.children[c] # shift node down a level 

        curr.word = word
                

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.res = set()

        # establish the Trie 
        trie = Trie() 
        for word in words: 
            trie.insert(word)
        
        # search for formed words in the list 
        root = trie.root 

        for i in range(len(board)):
            for j in range(len(board[i])):
                
                self.dfs(i, j, board, set(), root)
        

        return list(self.res)


    
    def dfs(self, row, col, board, seen, node):

        if (
            row >= len(board) or 
            row < 0 or 
            col >= len(board[0]) or 
            col < 0 or 
            (row, col) in seen or # seen this particular spot on the board before 
            board[row][col] not in node.children
        ):
            return 

        # update seen & the current node 
        curr_letter = board[row][col]
        node = node.children[curr_letter]
        seen.add((row, col))

        # check if current node is a word 
        if node.word is not None:
            self.res.add(node.word)
        
        # recrusively check all possible solution 
        self.dfs(row + 1, col, board, seen, node) 
        self.dfs(row - 1, col, board, seen, node) 
        self.dfs(row, col + 1, board, seen, node) 
        self.dfs(row, col - 1, board, seen, node)


        seen.remove((row, col))

        


