class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            
            curr = curr.children[c]
        
        curr.endOfWord = True 
        

    def search(self, word: str) -> bool:

        def dfs(index, node):

            for i in range(index, len(word)):

                curr = word[i]

                if curr == '.':
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True 
                    
                    return False 
                else:
                    if curr not in node.children:
                        return False 
                    
                    node = node.children[curr]
            
            return node.endOfWord
        
        return dfs(0, self.root)

