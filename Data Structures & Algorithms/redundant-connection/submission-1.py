class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adjList = {i: [] for i in range(1, len(edges) + 1)}

        def hasCycle():
            visited = set()
            
            def dfs(node, parent):
                visited.add(node)
                
                for nei in adjList[node]:
                    if nei == parent:
                        continue 
                    if nei in visited:
                        return True  # cycle detected 
                    if dfs(nei, node):
                        return True 
                
                return False
            
            # Check all components, not just starting from node 1
            for node in range(1, len(edges) + 1):
                if node not in visited:
                    if dfs(node, -1):
                        return True
            
            return False

        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)           

            if hasCycle():
                return [e1, e2]
        
        return []
