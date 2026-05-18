class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        self.parent = {i: i for i in range(1, len(edges) + 1)}
        
        for v1, v2 in edges:

            if not self.union(v1, v2):
                return [v1, v2]
    

    def find(self, x):
        if self.parent[x] == x:
            return x 
        
        root = self.find(self.parent[x])
        self.parent[x] = root # shorten it 

        return root 
    

    def union(self, v1, v2):

        v1_parent = self.find(v1)
        v2_parent = self.find(v2)

        print(f"v1_parent:{v1_parent}, v2_parent={v2_parent}")
        if v1_parent == v2_parent:
            return False 
        

        self.parent[v2_parent] = v1_parent
        return True 

        


        
    
