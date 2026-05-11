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

        def dfs(curr):
            if not curr:
                return None
            elif curr in mapping:
                return mapping[curr]
            
            clone = Node(curr.val)
            mapping[curr] = clone 

            cloned_neighbors = []
            for nei in curr.neighbors:
                cloned_neighbors.append(dfs(nei))
            
            clone.neighbors = cloned_neighbors 
            return clone
        

        return dfs(node)



