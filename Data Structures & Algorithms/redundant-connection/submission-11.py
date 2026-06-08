class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
            a) Itereate through edges
            b) Process the edge 
                --> add to adjancy list 
                --> determine if it caused a cycle 
                --> if it caused a cycle, return None 

            

            Solutions:
                Disjoint Union Set 
                    --> find (X) --> returns the "parent" node of the V 
                    --> union (X) --> sets the "parent" node of X to its parent
                    --> if find ends up returning 
                

                Every single vertex originally is going to have a parent of itself
                Once we "process" an edge [x,y], we can find the parent of [x] and [y]
                If these two are the same, then we can return the edge since we've found a cycle 
                If they aren't the same, then we go through and UNION the two 
                    --> parent of node Y becomes a child of parent of node X 
                

            Why can't we process this via a adjancy list? This is becuase of the "one-by-one" 
            nature of processingthis graph in order to return the "edge" that appear last. We 
            would need to go through and run a DFS each time we add a node, which is less efficient ??? 
                --> look into this 

            

            {1:1, 2:2, 3:3, 4:4}
                find(1) == 1
                find(2) == 2 

                union(1,2) --> sets 1 as the parent of 2 
            
            {1:1. 2:1, 3:3, 4:4}
                find(1) == 1
                find(3) == 3 

                union (1,3) --> sets 1 as the parent of of 3 
            
            {1:1, 2:1, 3:1, 4:4}
                find(3) == 1
                find(4) == 4

                union (1,4) --> sets 1 as parent of 4 
            
            {1:1, 2:1, 3:1, 4:1}
                find (2) == 1 
                find (4) == 1

                DUPLICATE!!
        """

        """
        {1:1, 2:2, 3:3, 4:4, 5:5}
            find(1) == 1 
            find(4) == 4

            union(1,4)
        
        {1:1, 2:2, 3:3, 4:1, 5:5}
            find(3) == 3
            find(4) == 1

            union(3,1)
        
        {1:3, 2:2, 3:3, 4:1, 5:5}
            find(1) == 3
            find(3) == 3

            union ()

        """

        # each vertex is originally a parent of itself
        self.dsu = {n: n for n in range(1, len(edges) + 1)}


        for v1, v2 in edges:

            # find the parents of v1 and v2 
            v1_parent = self.find(v1)
            v2_parent = self.find(v2)

            if v1_parent == v2_parent:
                return [v1,v2]
            

            # union if not 
            self.union(v1_parent, v2_parent)
        
        return None 

    def find(self, v):
        if v == self.dsu[v]:
            return v
        
        return self.find(self.dsu[v])
    

    def union(self, parent, child):

        self.dsu[child] = parent
        