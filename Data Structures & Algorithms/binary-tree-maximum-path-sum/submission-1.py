# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        self.dfs(root)
        return self.res 
    
    def dfs(self, root):
        if not root:
            return 0

        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))

        self.res = max(self.res, root.val + left + right)

        return max(left, right) + root.val 
