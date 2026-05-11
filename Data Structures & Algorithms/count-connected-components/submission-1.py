class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # build adjacency list 
        adjList = {i: [] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        

        visited = set() 

        def dfs(node):
            if node in visited:
                return
            

            visited.add(node)
            for nei in adjList[node]:
                dfs(nei)
        
        
        num_connected = 0 
        for i in range(n):
            if i not in visited:
                dfs(i)
                num_connected += 1
        
        return num_connected 
