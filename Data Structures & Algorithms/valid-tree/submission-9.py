class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """

        What is a valid tree?
            - no cycles 
            - all nodes are connected
        
        Create an adjacency list for dependencies 

        DFS on ADJ List ensuring all nodes are visited and no cycles are found
        """

        # create adj list 
        adjList = {i: [] for i in range(n)}
        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)


        # given this is undirected, account for previous value to ensure we don't induce cycle 
        visited = set() 
        def dfs(node, prev):
            if node in visited:
                return False 
            
            visited.add(node)
            for nei in adjList[node]:
                if nei != prev and not dfs(nei, node):
                    return False 
            
            return True 
        

        return dfs(0, None) and len(visited) == n




