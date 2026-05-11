class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        adjList = {i: [] for i in range(1, n + 1)}
        for src, target, time in times:
            adjList[src].append((target, time))


        # visited = {node: min_time_to_node}
        visited = {}

        heap = [] 
        heapq.heappush(heap, (0, k))

        while heap:

            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            
            visited[node] = cost 

            # process neighbors 
            for nei, nei_cost in adjList[node]:

                if nei not in visited:
                    heapq.heappush(heap, (nei_cost + cost, nei))
            
        

        return max(visited.values()) if len(visited) == n else -1




                