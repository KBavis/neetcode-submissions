class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.root = TrieNode() 
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                
                curr = curr.children[c]
            
            curr.word = word 

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                curr = board[i][j]
                self.search(i,j,set(), board, self.root, result)
        
        return list(result)

    
    def search(self, i, j, seen, board, node, result):
        if (i,j) in seen or i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] not in node.children:
            return 
        
        seen.add((i,j))
        c = board[i][j]
        node = node.children[c]


        if node.word:
            result.add(node.word)
            node.word = None 
        

        self.search(i - 1, j, seen, board, node, result)
        self.search(i + 1, j, seen, board, node, result)
        self.search(i, j + 1, seen, board, node, result)
        self.search(i, j - 1, seen, board, node, result)


        seen.remove((i,j))
        




        