# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # compute mapping of value to index in inorder 
        mapping = {val: i for i, val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(left, right):
            if left > right:
                return None 
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1 
            root = TreeNode(root_val)

            inorder_idx = mapping[root_val]

            root.left = dfs(left, inorder_idx - 1)
            root.right = dfs(inorder_idx + 1, right)

            return root 
        

        return dfs(0, len(inorder) - 1)

            
        
