# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        res = [] 
        if not root:
            return res

        q = deque([root])

        while q:

            level_nodes_len = len(q)
            curr = []
            for i in range(level_nodes_len): 
                
                curr_node = q.popleft() 
                curr.append(curr_node.val)

                # process children 
                if curr_node.left:
                    q.append(curr_node.left)
                
                if curr_node.right:
                    q.append(curr_node.right)
            

            # append to res 
            res.append(curr)
        

        return res 
            