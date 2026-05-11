# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
            a) 1-index (meaning that the left most node in BST is going to be 1)
            b) 


                6
            /       \ 
         3
       /    \ 
    2          4

            Transverse as deep left as we can and find left most node 
            
            Inorder transveral and we can increment our current value of k in order to check 
        """

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
            
