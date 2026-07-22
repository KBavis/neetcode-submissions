class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
            Graphs 
                - directed graph (can only go from certain locations to other locations)
                
            Cost associated with the flights themselves and the goal is to minimize that cost 

            We only have K number of stops to get to the destination from the src 

            Idea:
                - adj list to represent dependencies 
                    --> mapping of src to list of destinations
                    --> 1: [(3, 100), (2, 100)]
                - at each point, we're going to choose the minimum cost to travel in that direction 
                - numStops is initally zero, only increments after we've arrived at new destination 

                - kruskals algorithm 
                    --> minimum spanning tree 
                    --> leveraging a minHeap 
                        --> process neighbors 
                

                stop going path when the current number of stops >= k and not at destination 
        """

        # inialize the adj list 
        adjList = {i: [] for i in range(n)}
        for curr_src, curr_dst, cost in flights:
            adjList[curr_src].append((cost, curr_dst))
        
        """
            1: [(100, 2), (300, 3)]
        """


        # initlaize min heap with potential locations from the src (num_stops set to zero initally)
        if not adjList[src]:
            return -1

        min_heap = []
        for cost, curr_dst in adjList[src]:
            heapq.heappush(min_heap, (cost, 0, curr_dst))
        
        while min_heap:

            # extract the current cheapest route
            curr_cost, num_stops, curr_stop = heapq.heappop(min_heap)

            # check if we've exceeded our allocated of stops
            if num_stops > k:
                continue 

            # check if we've reached our destination
            if curr_stop == dst:
                return curr_cost 


            # process the neighbors 
            for nei_cost, nei_stop in adjList[curr_stop]:
                heapq.heappush(min_heap, (nei_cost + curr_cost, num_stops + 1, nei_stop))

        
        # never reached desintation via allocated number of stops 
        return -1
        

