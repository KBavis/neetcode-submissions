# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        res = [] 
        if not root:
            return res 

        q = deque([root])
        while q:

            length = len(q)
            for i in range(length):

                curr_node = q.popleft() 

                # only append if right-most position on level 
                if i == length - 1:
                    res.append(curr_node.val)
                
                # process children
                if curr_node.left:
                    q.append(curr_node.left)
                
                if curr_node.right:
                    q.append(curr_node.right)
        
        return res

