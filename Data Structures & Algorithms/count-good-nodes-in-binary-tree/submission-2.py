# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       
        self.count = 0 


        def dfs(curr, curr_max):
            if not curr:
                return 
            
            if curr.val >= curr_max:
                curr_max = curr.val 
                self.count += 1 
            

            dfs(curr.left, curr_max)
            dfs(curr.right, curr_max)
        

        dfs(root, float('-inf'))

        return self.count