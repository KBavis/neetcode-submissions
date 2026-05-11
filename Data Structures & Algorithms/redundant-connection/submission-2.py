class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        


        def hasCycle():

            visited = set()

            def dfs(node, parent):
                if node in visited: 
                    return True 
                
                visited.add(node)
                for nei in adjList[node]:
                    if nei != parent and dfs(nei, node):
                        return True
                
                return False 


            for node in range(1, len(edges) + 1):
                if node not in visited and dfs(node, None):
                    return True 

            return False 
        
        adjList = defaultdict(list)

        # build adjancency list incrementally 
        for e1, e2 in edges: 
            adjList[e1].append(e2)
            adjList[e2].append(e1)

            if hasCycle():
                return [e1, e2]
        
        return [] 



