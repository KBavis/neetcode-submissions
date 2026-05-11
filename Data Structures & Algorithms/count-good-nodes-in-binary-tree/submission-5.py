# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        """
            Goal:
                Transverse down through a tree
                Keep a running "current max" 
                If current node value >= current max, then update current max 


                3 
            3       None 
        4      2
        """


        self.good_nodes = 0 

        def dfs(node, curr_max):
            if not node:
                return 
            

            if node.val >= curr_max:
                self.good_nodes += 1 
                curr_max = node.val 
            

            dfs(node.left, curr_max)
            dfs(node.right, curr_max) 
        

        dfs(root, float('-inf'))
        return self.good_nodes 
        

