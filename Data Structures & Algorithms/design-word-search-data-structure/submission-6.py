class Node:
    def __init__(self):
        self.isWord = False 
        self.children = {} 

class WordDictionary:

    def __init__(self):
        self.root = Node() 
        

    def addWord(self, word: str) -> None:
        curr = self.root 

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node() 
            
            curr = curr.children[c]
        
        curr.isWord = True 
        

    def search(self, word: str) -> bool:


        def dfs(idx, curr):

            for i in range(idx, len(word)):

                c = word[i]

                if c == ".":
                    
                    # recurse through children 
                    for child in curr.children.values(): 
                        if dfs(i + 1, child):
                            return True 
                    
                    # no match at all 
                    return False 
                        
                else:
                    if c not in curr.children:
                        return False 
                    
                    curr = curr.children[c]
            
            return curr.isWord 
        

        return dfs(0, self.root)
        
