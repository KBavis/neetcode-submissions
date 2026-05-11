class Node:
    def __init__(self):
        self.children = {} 
        self.word = False 

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root 

        for c in word: 
            if c not in curr.children:
                curr.children[c] = Node() 
            
            curr = curr.children[c]
        
        curr.word = True 
        

    def search(self, word: str) -> bool:

        def dfs(node, index):

            for i in range(index, len(word)):
                c = word[i]

                if c == '.':
                    for curr in node.children.values():
                        if dfs(curr, i + 1):
                            return True 
                    
                    return False 
                else:
                    if c in node.children:
                        node = node.children[c]
                    else:
                        return False 
            
            return node.word
        
        return dfs(self.root, 0)
            


        
