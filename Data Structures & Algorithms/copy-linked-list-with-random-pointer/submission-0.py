"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        """
            1. Creating a deep copy 
            2. Each node in deep copy needs to contain the original next node (that's copied) and orignal random node (that's copied)
            3. Recursive solution? Mapping of {OG Node: Copy Node}
            4. Base case (we have copied this node before)
        """

        clones = {}

        def dfs(curr):
            if curr == None:
                return None
            elif curr in clones:
                return clones[curr]
            
            clone = Node(curr.val)
            clones[curr] = clone

            clone.next = dfs(curr.next)
            clone.random = dfs(curr.random)

            return clone 
        

        return dfs(head)