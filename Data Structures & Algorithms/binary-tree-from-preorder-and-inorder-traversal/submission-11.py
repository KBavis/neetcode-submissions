# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # PREORDER = [root, left, right]
        # INORDER = [left, root, right]

        mapping = {val: i for i, val in enumerate(inorder)}
        self.preorder_idx = 0

        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1 

            root = TreeNode(root_val)

            idx = mapping[root_val]

            root.left = dfs(left, idx - 1)
            root.right = dfs(idx + 1, right)

            return root


        return dfs(0, len(inorder) - 1)