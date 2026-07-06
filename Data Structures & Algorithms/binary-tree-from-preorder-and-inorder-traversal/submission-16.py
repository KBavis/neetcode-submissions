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

        # inorder mapping 
        self.mapping = {}
        for i, val in enumerate(inorder):
            self.mapping[val] = i

        self.preorder_idx = 0 
        return self.optimize(0, len(inorder) - 1)

        # return self.brute_force(preorder, inorder)


    def optimize(self, left, right):
        if left > right:
            return None 
        

        root_val = preorder[self.preorder_idx]
        self.preorder_idx += 1 

        inorder_idx = self.mapping[root_val]

        root = TreeNode(root_val)
        root.left = self.optimize(left, inorder_idx - 1)
        root.right = self.optimize(inorder_idx + 1, right)

        return root
        

        



    def brute_force(self, preorder, inorder):
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

