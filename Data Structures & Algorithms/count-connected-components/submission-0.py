class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        visited = set()

        def dfs(node, prevNode):
            if node in visited:
                return 
            
            visited.add(node)

            for neighbor in adjList[node]:
                if neighbor == prevNode:
                    continue 

                dfs(neighbor, node)

        
        total = 0
        for i in range(n): 
            if i not in visited:
                dfs(i, -1)
                total += 1
        

        return total

        