# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.good_count = 0 

        def dfs(curr, curr_max):
            if not curr:
                return 
            
            if curr.val >= curr_max:
                self.good_count += 1 
                curr_max = curr.val
            

            dfs(curr.left, curr_max)
            dfs(curr.right, curr_max)
        

        dfs(root, float('-inf'))
        return self.good_count 