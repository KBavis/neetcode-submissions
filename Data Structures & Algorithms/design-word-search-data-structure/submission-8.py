class Node:

    def __init__(self):
        self.children = {}
        self.isWord = False 

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

        def dfs(node, idx):
            if not node:
                return False 

            curr = node 
            for i in range(idx, len(word)):

                letter = word[i]

                # recurse through each child
                if letter == ".":
                    for c in curr.children:
                        if dfs(curr.children[c], i + 1):
                            return True 
                    
                    return False 
                # check normally 
                else:
                    
                    if letter not in curr.children:
                        return False 
                    else:
                        curr = curr.children[letter]
            

            return curr.isWord 

        return dfs(self.root, 0)
        
