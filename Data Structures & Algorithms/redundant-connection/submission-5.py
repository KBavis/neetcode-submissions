class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        def hasCycle(new_node):

            visited = set() 

            def dfs(node, parent):
                if node in visited:
                    return True 
                

                visited.add(node)
                for nei in adjList[node]:
                    if parent != nei and dfs(nei, node):
                        return True 
                
                return False 
            
            return dfs(new_node, None)
        
        # build the adjacency list step at a time and check for cycles 
        adjList = defaultdict(list)
        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)

            if hasCycle(e1):
                return [e1, e2]
        

        return []



