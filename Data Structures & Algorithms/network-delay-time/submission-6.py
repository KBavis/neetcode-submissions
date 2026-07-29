class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
            From startPoint = k, touch all the nodes in minimum time 

            Mapping:
                source_node --> [(time, potential destination)]

            First populate heap with mapping[source_nodes]
                - min heap to have the optimal route 

            Visited (Node)
                - once a node is visited, its gaurnateed to be the fastest way to get to that node

            Cotninue adding to the heap as we search 
                --> stop searching once the heap is empty 
                --> visited == n 
        """
        
        # create adj list
        adjList = {i: [] for i in range(1, n + 1)}
        for entry in times:
            source, target, time = entry[0], entry[1], entry[2]
            adjList[source].append((time, target))
        

        # initalize heap 
        min_heap = []
        for nei in adjList[k]:
            heapq.heappush(min_heap, nei)
        
        visited = set() 
        visited.add(k)

        # process records 
        while min_heap:

            time_from_k, node = heapq.heappop(min_heap)

            # check if we've seen a record before
            if node in visited:
                continue 
            
            # mark node as visited and accumulate in total time
            visited.add(node)

            # check if reached all nodes
            if len(visited) == n:
                return time_from_k

            # process neighbors of current node 
            for nei in adjList[node]:
                if nei[1] not in visited:
                    heapq.heappush(min_heap, (time_from_k + nei[0], nei[1]))
        
        
        return -1 
        
            



