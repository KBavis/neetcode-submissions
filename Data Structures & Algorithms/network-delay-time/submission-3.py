class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        min_time = float('inf')

        adjList = {i: {} for i in range(1, n + 1)}
        for t1, t2, cost in times:
            adjList[t1][t2] = cost 
        
        print(adjList)

        min_heap = []
        heapq.heappush(min_heap, (0, k))
        visited = {}

        while min_heap:

            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue 
            

            visited[node] = cost 

            for nei, curr_cost in adjList[node].items():
                heapq.heappush(min_heap, (curr_cost + cost, nei))
        

        return max(visited.values()) if len(visited) == n else -1
