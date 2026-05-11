# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder --> list[0] == root 
        # inorder --> index of root in inorder (to the left, num nodes in left tree, right, num right tree)

        # create inorder mapping 
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        

        self.pre_idx = 0 
        def construct(left, right):
            if left > right:
                return 
            

            # extract root value 
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(root_val)
            
            
            idx = inorder_idx[root_val]

            node.left = construct(left, idx - 1)
            node.right = construct(idx + 1, right)

            return node 
        

        return construct(0, len(inorder) - 1)