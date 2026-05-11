# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return 
            
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        nodes = data.split(",")
        self.idx = 0 

        def dfs():
            if nodes[self.idx] == "N":
                self.idx += 1 
                return None 
            
            curr_val = nodes[self.idx]
            root = TreeNode(curr_val)
            self.idx += 1 
            
            root.left = dfs() 
            root.right = dfs() 

            return root 
        
        return dfs()