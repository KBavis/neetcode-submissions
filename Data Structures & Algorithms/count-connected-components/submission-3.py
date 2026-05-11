class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # build adj list 

        # transverse a particular node (find all connections) 

        # maintain a set of seen components 

        # return back 


        adjList = {i: set() for i in range(n)}
        for e1, e2 in edges:
            adjList[e1].add(e2)
            adjList[e2].add(e1)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return


            visited.add(node)
            for nei in adjList[node]:
                dfs(nei)


        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i) 
                count += 1 


        return count 
