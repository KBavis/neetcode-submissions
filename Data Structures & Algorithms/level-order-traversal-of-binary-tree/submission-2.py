# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return [] 
        

        q = deque([root])
        result = [] 

        while q:

            length = len(q)
            level = [] 

            for i in range(length):
                curr = q.popleft() 
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
            result.append(level)
    

        return result 
                