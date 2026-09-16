class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
            - set of edges (undirected)
            - graph problem (adjacency list)
                --> allows to transverse around to neighbors 
            - multiple answers, but we want to return the last input in edges 


            --> build the solution incrementally 
                --> Disjoint Union Set 
                    --> find function (returns the parent)
                    --> union function (assings a parent node)
        """
    
        child_to_parent = {i: i for i in range(1, len(edges) + 1)}
        def find(x):
            """
                Find the parent of X 
            """
            if x == child_to_parent[x]:
                return x 
            
            parent = find(child_to_parent[x])
            child_to_parent[x] = parent 
            return parent 


        for v1, v2 in edges:

            v1_parent = find(v1)
            v2_parent = find(v2)

            # if they have the same parent, a cycle has been found 
            if v1_parent == v2_parent:
                return [v1, v2]

            # if not, we merge them 
            child_to_parent[v2_parent] = v1_parent 
        
        return []

