class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # adjacency list 
        adjList = {i: [] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        

        visited = set() 

        def dfs(curr, prev):
            if curr in visited:
                return False
            


            visited.add(curr)
            for nei in adjList[curr]:
                if nei == prev:
                    continue 

                if not dfs(nei, curr):
                    return False 

            return True 
        

        
        return dfs(0, None) and n == len(visited)
        


            

