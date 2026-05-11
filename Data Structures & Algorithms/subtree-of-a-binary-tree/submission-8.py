# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True 
        elif not root or not subRoot:
            return False 
        
        # is subRoot a subtree of root? 
        isSubRoot = self.isSameTree(root, subRoot)
        if isSubRoot:
            return True 
        

        # check children of root 
        return (
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        )



    

    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True 
        elif not root1 or not root2:
            return False 
        elif root1.val != root2.val:
            return False 
        

        return (
            self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        )