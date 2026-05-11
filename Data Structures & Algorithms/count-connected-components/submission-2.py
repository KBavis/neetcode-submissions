class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # build adjacency list 
        adjList = {i: [] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])


        # set for visited nodes     
        visited = set() 

        def dfs(n):
            if n in visited:
                return 
            

            visited.add(n)
            
            # recurse through graph 
            neighbors = adjList[n]
            for nei in neighbors: 
                dfs(nei)
            





        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1 
            
        
        return count 

 
