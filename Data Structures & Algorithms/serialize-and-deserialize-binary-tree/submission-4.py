# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        nodes = [] 

        def dfs(node):
            if not node:
                nodes.append("N")
                return 
            
            nodes.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        

        dfs(root)

        return ",".join(nodes)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        nodes = data.split(",")
        self.idx = 0 

        def dfs():
            if nodes[self.idx] == "N":
                self.idx += 1 
                return None 
            

            node = TreeNode(nodes[self.idx])
            self.idx += 1 

            node.left = dfs()
            node.right = dfs()

            return node 
        
        return dfs()
