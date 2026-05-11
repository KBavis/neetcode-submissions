# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(root):
            if not root:
                result.append('N')
                return 
            
            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        nodes = data.split(",")
        self.i = 0

        def dfs():
            if nodes[self.i] == 'N':
                self.i += 1
                return None
            
            root = TreeNode(int(nodes[self.i]))
            self.i += 1

            root.left = dfs()
            root.right = dfs()

            return root 
        
        return dfs()

