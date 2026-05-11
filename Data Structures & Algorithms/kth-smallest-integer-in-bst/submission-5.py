# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
        WANT: Find the kth smallest node in the tree

        What is the smallest? --> The node all the way to the LEFT 
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        self.k = k 
        self.val = None

        def dfs(curr):
            if not curr or self.val != None:
                return


            dfs(curr.left)

            self.k -= 1
            if self.k == 0:
                self.val = curr.val 
                return 

            dfs(curr.right)


        dfs(root)

        return self.val