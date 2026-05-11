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
        
        dummy = Node(-1) 
        new_head = dummy 

        cloned_nodes = {} 

        
        def search(node):
            if not node:
                return None 
            elif node in cloned_nodes:
                return cloned_nodes[node]
            

            clone = Node(node.val)
            cloned_nodes[node] = clone 

            clone.next = search(node.next)
            clone.random = search(node.random)

            return clone 


        return search(head)
