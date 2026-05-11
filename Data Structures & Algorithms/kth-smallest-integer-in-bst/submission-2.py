# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.k = k 

        self.dfs(root, k)
        return self.res
    

    def dfs(self, root, k):
        if not root:
            return 
        
        self.dfs(root.left, k)

        self.k -= 1
        if self.k == 0:
            self.res = root.val 
        
        self.dfs(root.right, k)

        
