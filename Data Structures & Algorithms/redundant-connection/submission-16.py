class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
            With a problem like this, there are basicaly two outcomes:

            1) brute force 
                --> continuouslly do cycle detection, building up your adj list and rerunning DFS to determine if any cycles exist
                --> once you find one that cuases a cycle, you ahve found the edge in question 
                --> O(E * (V + E))
                        --> we need to iterate through each edge, and then apply DFS algorith,
                        --> even with memoization, we will bascially be performing an O(V +E algorithm E times)
            
            2) incremental 
                --> leveraging a Disjoint Union Set 
                --> consistnetly building our Graph up, edge by edge, until we find one that results in a cycle
        """


        # each node ends up being being a parent of itself initially 
        parent_nodes = {} 
        for i in range(1, len(edges) + 1):
            parent_nodes[i] = i 

        
        # define function for finding parent 
        def find(curr):

            # base case: stop once the parent of current node is itself
            if parent_nodes[curr] == curr:
                return curr 
            
            # find parent, and set for current node 
            curr_parent = find(parent_nodes[curr])
            parent_nodes[curr] = curr_parent 
            return curr_parent 

        
        # iterate through the edges and apply find() and union() 
        for e1, e2 in edges:

            e1_parent = find(e1)
            e2_parent = find(e2)

            if e1_parent == e2_parent:
                return [e1, e2]
            
            # set E2 parent to be the parent of E1 
            parent_nodes[e2_parent] = e1_parent 
        

        return edges[-1]

