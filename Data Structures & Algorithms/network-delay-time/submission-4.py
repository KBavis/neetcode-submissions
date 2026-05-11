class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """ 
            0. setup adj list for our directed graph 
                [src_node][neighbor] = time

            a) Start a source node 
            b) Add all potential neighbors to a min heap, ordered by time 
            c) Always take smallest route 

            How to account for "seeing" a node already, but it not being the minimum amount time 
            to get to that node 
                --> prev node ? making sure we don't go to neighbor if its the previous one 


            -- dictionary storing seen nodes and the corresponding minimum time to get to that node 
            -- min heap that stores relevant neighbors, ordered by smallest to get there 
            -- prev node to make sure we don't go right back to old node 

            ... Return the time accumualted ONLY IF the visited set is equal to the number of nodes present 
        """


        min_time = float('inf')


        adjList = {i: {} for i in range(1, n + 1)}
        for t1, t2, cost in times:
            adjList[t1][t2] = cost 
        

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
