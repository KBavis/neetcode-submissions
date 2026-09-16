class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # 1. build adj list 
        adjList = {i: [] for i in range(1, n + 1)}
        for source, target, cost in times:
            adjList[source].append((cost, target))
        

        # 2. bfs from starting poistion 
        min_heap = [(0, k)]
        visited = set() 


        while min_heap: 

            cost, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue 
            

            visited.add(curr_node)
            if len(visited) == n:
                return cost 
            

            # 3. process neighbors 
            for nei_cost, nei_node in adjList[curr_node]:
                if nei_node not in visited:
                    heapq.heappush(min_heap, (nei_cost + cost, nei_node))


        return -1  
