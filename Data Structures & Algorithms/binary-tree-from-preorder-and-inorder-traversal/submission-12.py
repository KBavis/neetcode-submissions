# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
            - preorder --> first node is the "root" 
            - inorder --> find the root, everything to the left of it is going to be in left subtree, everything right in right subtree 
        """

        # return self.naive_solution(preorder, inorder)
        return self.optimal_solution(preorder, inorder)


    def optimal_solution(self, preorder, inorder):

        inorder_to_idx = {}
        for i, val in enumerate(inorder):
            if val not in inorder_to_idx:
                inorder_to_idx[val] = deque([])
            
            inorder_to_idx[val].append(i)
        
        print(inorder_to_idx)

        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None 
        
            root_val = preorder[0]
            root = TreeNode(root_val)
            root_idx = inorder_to_idx[root_val].popleft() 

            root.left = self.naive_solution(preorder[1:root_idx + 1], inorder[:root_idx])
            root.right = self.naive_solution(preorder[root_idx + 1:], inorder[root_idx + 1:]) 

            return root
        
        return dfs(preorder, inorder)


    def naive_solution(self, preorder, inorder):
        if not preorder or not inorder:
            return None 
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val)

        root.left = self.naive_solution(preorder[1:root_idx + 1], inorder[:root_idx])
        root.right = self.naive_solution(preorder[root_idx + 1:], inorder[root_idx + 1:]) 

        return root 