class TrieNode:

    def __init__(self):
        self.children = {} 
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
            Need an efficient way for 
                a) determining a valid word 
                b) appending that "valid" word to a result set 
                c) determining if a next character is continuation of a valid word 
                d) even if we find a valid word (i.e back), there could be an additional valid word (i.e backer)
            
            Screams TRIE data strucutre along with a DFS functionality 
        """


        trie = self.get_trie(words)

        self.res = [] 

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, trie, set())


        return self.res
    

    def dfs(self, row, col, board, curr_node, visited):
        if (
            row >= len(board) or 
            col >= len(board[0]) or 
            col < 0 or 
            row < 0 or 
            (row, col) in visited or
            board[row][col] not in curr_node.children
        ):
            return
        

        # update node 
        curr_character = board[row][col]
        node = curr_node.children[curr_character]

        # add node to visited
        visited.add((row, col))

        # determine if the current node is a valid word 
        if node.word:
            self.res.append(node.word)
            node.word = None
        
        # check neighbors for other words 
        self.dfs(row + 1, col, board, node, visited)
        self.dfs(row - 1, col, board, node, visited)
        self.dfs(row, col + 1, board, node, visited)
        self.dfs(row, col - 1, board, node, visited)

        # backtrack 
        visited.remove((row, col))



    def get_trie(self, words: List[str]):

        root_node = TrieNode()

        for word in words:
            self.insert_word(root_node, word)
        
        return root_node 
    

    def insert_word(self, root_node, word):

        curr_node = root_node

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            
            curr_node = curr_node.children[c]
        
        curr_node.word = word