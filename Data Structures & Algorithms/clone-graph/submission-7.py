"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        real_to_clone = {}

        def dfs(node, prev):
            if node in real_to_clone:
                return real_to_clone[node]
            
            # create clone and update mapping
            clone = Node(node.val)
            real_to_clone[node] = clone 

            # clone neighbors 
            cloned_neighbors = []
            for nei in node.neighbors:
                cloned_neighbors.append(dfs(nei, node))
            

            clone.neighbors = cloned_neighbors
            return clone 
        

        return dfs(node, None)

