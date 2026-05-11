class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root 

        for c in word:
            if c not in curr.children:
                return False 
            curr = curr.children[c]
        
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False 
            
            curr = curr.children[c]
        
        return True
        
        