class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        adjList = {i: {} for i in range(1, n + 1)}
        for src, target, time in times:
            adjList[src][target] = time 

        print(adjList)

        # visited = {node: min_time_to_node}
        visited = {i: float('inf') for i in range(1, n + 1)}
        print(visited)

        def dfs(node, total_time):
            if total_time >= visited[node]:
                return 
            
            visited[node] = total_time

            neighbors = adjList[node]
            for target, time in neighbors.items():
                dfs(target, total_time + time)
        
        dfs(k, 0)

        max_time = max(visited.values())
        return max_time if max_time != float('inf') else -1

                