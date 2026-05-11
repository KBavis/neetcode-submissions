# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        # dfs all the way down

        # passing "max" value (which is initally root)

        # copare current node to max value, and if less, add as good node 

        self.num_good_nodes = 0

        def dfs(node, max_value):
            if not node:
                return 
            

            if node.val >= max_value:
                self.num_good_nodes += 1 
            
            max_value = max(node.val, max_value)

            dfs(node.left, max_value)
            dfs(node.right, max_value)
        

        dfs(root, root.val)

        return self.num_good_nodes
            

