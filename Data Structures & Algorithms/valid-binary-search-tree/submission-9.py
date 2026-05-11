# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True 

        
        def dfs(root, max_val, min_val):
            if not root:
                return True 
            
            if not (min_val < root.val < max_val):
                return False 
            

            return dfs(root.left, root.val, min_val) and dfs(root.right, max_val, root.val)
        

        return dfs(root, float('inf'), float('-inf'))