# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.k = k
        self.kth = None
        
        def dfs(root):
            if not root:
                return 
            

            dfs(root.left)

            self.k -= 1 
            if self.k == 0:
                self.kth = root.val
                return

            dfs(root.right)
        

        dfs(root)

        return self.kth