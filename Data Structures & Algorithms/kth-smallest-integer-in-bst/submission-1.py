# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # left node 
        # root 
        # right 

        self.k = k
        self.result = None
        self.dfs(root)
        return self.result
    
    def dfs(self, root):
        if not root:
            return 
        
        self.dfs(root.left)

        self.k -= 1
        if self.k == 0:
            self.result = root.val

        self.dfs(root.right)
