class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        self.parent = {i: i for i in range(1, len(edges) + 1)}
        
        for e1, e2 in edges:

            p1, p2 = self.find(e1), self.find(e2)

            # already connected, redundant so return edge
            if p1 == p2:
                return [e1, e2]
            
            # union 
            self.parent[p1] = p2
        
        return [] 



    def find(self, node):
        """
        Find the nodes parent 
        """

        # if this node is the parent of itself, return node 
        if node == self.parent[node]:
            return node
        
        # compress the path 
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]




