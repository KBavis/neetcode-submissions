# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        self.curr = k 
        self.val = None 

        def dfs(node):
            if not node:
                return 
            elif self.val:
                # terminate early if we found the value 
                return
            

            dfs(node.left)

            self.curr -= 1 
            if self.curr == 0:
                self.val = node.val 
                return 
            

            dfs(node.right)
        

        dfs(root)
        return self.val 
            
