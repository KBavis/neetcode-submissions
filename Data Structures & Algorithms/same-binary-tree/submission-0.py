# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)

    
    def dfs(self, root1, root2):
        if not root1 and not root2:
            return True 
        elif not root1 or not root2:
            return False 
        
        if root1.val != root2.val:
            return False

        left = self.dfs(root1.left, root2.left)
        right = self.dfs(root1.right, root2.right)

        return left and right
        