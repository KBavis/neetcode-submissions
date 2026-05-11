"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        mapping = {}

        def dfs(node):
            if not node:
                return None
            elif node in mapping:
                return mapping[node]

            clone = Node(node.val)
            mapping[node] = clone
            
            cloned_neighbors = []
            for neighbor in node.neighbors:
                cloned_neighbors.append(dfs(neighbor))
            
            clone.neighbors = cloned_neighbors 

            return clone 
        

        return dfs(node)
            

        