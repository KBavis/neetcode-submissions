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
        
            clone = Node(node.val)
            clones[node] = clone 

            cloned_neighbors = [] 
            for nei in node.neighbors:
                cloned_neighbors.append(dfs(nei))
        
            clone.neighbors = cloned_neighbors 
            return clone 
    

        return dfs(node) if node else None
        