"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]
            
            cloned_node = Node(node.val) 
            clones[node] = cloned_node 

            cloned_neis = []
            for nei in node.neighbors:
                cloned_neis.append(dfs(nei)) 
            
            cloned_node.neighbors = cloned_neis 
        
            return cloned_node 
        

        return dfs(node) if node else None
