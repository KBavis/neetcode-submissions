# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None 
        
        root_val = preorder[0]
        root = TreeNode(val=root_val)

        # find idx of root in inorder
        root_idx = inorder.index(root_val)

        root.left = self.buildTree(preorder[1: 1 + root_idx], inorder[0: root_idx])
        root.right = self.buildTree(preorder[1 + root_idx:], inorder[root_idx + 1:])

        return root 
        
