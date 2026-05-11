class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjList = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False 
            

            visited.add(node)

            for nei in adjList[node]:
                if nei != parent and not dfs(nei, node):
                    return False 
            
            return True 
        

        if not dfs(0, -1):
            return False 
        

        return len(visited) == n
            