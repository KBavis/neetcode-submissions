class TrieNode():
    def __init__(self):
        self.children = {} 
        self.word = None 


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
            Notes:
                - cells can be re-used across multiple words 
                - cell cannot be used more than once in a word (need a set to track seen positions)
                - need a way to easily determine if we "found" a word 
                - Trie data structure is optimal for doing this 
                    - check if the root node contains current character as we iterate through 
                    - if it does, then we start searching via dfs (updating curr node as we go) 
                    - if we find a node that is a "word" we should continue searching (ca, can) could both be words 


            We solved word search I but not word search II 

                - we could in theory just use a set() in order to ensure our res is unique 
                - we could also "remove" the word from valid list 
        """

        root_node = self.get_trie(words)

        self.res = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root_node.children:
                    self.dfs(i, j, set(), board, root_node)
        
        return self.res 



    def dfs(self, row, col, seen, board, curr_node):
        if (
            row >= len(board) or 
            col >= len(board[0]) or 
            col < 0 or 
            row < 0 or 
            (row, col) in seen or 
            board[row][col] not in curr_node.children
        ):
            return 
        

        seen.add((row, col))

        # check if we found a word 
        curr_char = board[row][col]
        curr_node = curr_node.children[curr_char]   
        if curr_node.word is not None:
            self.res.append(curr_node.word)
            curr_node.word = None # ensure we don't use word again in future 
        

        # explore other directions for more words 
        self.dfs(row + 1, col, seen, board, curr_node)
        self.dfs(row - 1, col, seen, board, curr_node)
        self.dfs(row, col + 1, seen, board, curr_node)
        self.dfs(row, col - 1, seen, board, curr_node)

        seen.remove((row, col))

    

    def get_trie(self, words: List[str]): 
        root = TrieNode() 

        for word in words: 
            self.insert_word_into_trie(word, root)
        
        return root

    
    def insert_word_into_trie(self, word, root):
        
        curr = root 
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() 
            
            curr = curr.children[c]
        
        curr.word = word 
    
        

        