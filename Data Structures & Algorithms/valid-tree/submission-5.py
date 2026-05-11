class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # adj list 
        adjList = {i: [] for i in range(n)}
        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)

            # edge 1 : [edge2, edge3]
            # edge 2: [edge1, edge4]

        # dfs 
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False 
            
            visited.add(node)
            neighbors = adjList[node]

            for nei in neighbors:
                if nei != prev and not dfs(nei, node):
                    return False 
            
            return True 



        if not dfs(0, None):
            return False 
        
        return len(visited) == n
        
        