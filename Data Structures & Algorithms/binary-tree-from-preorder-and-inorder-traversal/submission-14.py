# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Preorder --> [Root, Left, Right]
        Inorder --> [Left, Root, Right]

        We know preorder[0] --> root 
            Finding the index of root in inorder --> IDX 
            [0, IDX) --> Left Sub Tree 
            [IDX + 1, rest of lenght] --> Right Sub Tree 
        

        Recursively solve
        """

        return self.recurse(preorder, inorder)
    


    def recurse(self, preorder, inorder):
        if not preorder or not inorder:
            return None 
        
        # extract root value 
        root_value = preorder[0]

        # find the index in inorder of root 
        root_idx_inorder = inorder.index(root_value) 

        curr = TreeNode(root_value)
        curr.left = self.recurse(preorder[1: 1 + root_idx_inorder], inorder[0 : root_idx_inorder])
        curr.right = self.recurse(preorder[1 + root_idx_inorder:], inorder[root_idx_inorder + 1:])

        return curr 

