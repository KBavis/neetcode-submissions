"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        original_to_clone = {}

        def dfs(curr):
            if curr in original_to_clone:
                return original_to_clone[curr]

            clone = Node(curr.val) 
            original_to_clone[curr] = clone
            cloned_nei = [] 

            for nei in curr.neighbors:
                cloned_nei.append(dfs(nei))
            
            clone.neighbors = cloned_nei 
            return clone 
        

        return dfs(node) if node else None