class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
            Purpose: ensure first a) you can reach destination in k stops, and then b) return the minimum 
            cost to reach that destination 

            Idea: Kruskal's Algorithm 
                - start at src 
                - derive minimum spannign tree starting at src 
                - just because your able to reach destination, doesn't necessarily mean tht it's the cheapest way 
        """


        # 1. derive adj list to understand neighbors
        adjList = {i: [] for i in range(n)}
        for curr_src, curr_dst, curr_cost in flights:
            adjList[curr_src].append((curr_cost, curr_dst))
        

        # 2. initalize queue with src
        min_heap = [(0, -1, src)]

        # 3. track minimum cost to arrive at destination & seen airports 
        min_cost = float('inf')
        seen = set()
        best = {}
        
        # 4. iterate while min heap isn't empty 
        while min_heap: 

            # 4a. pop the current vertex 
            curr_cost, curr_stops, curr_loc = heapq.heappop(min_heap)
            if curr_loc in seen:
                continue 

            # 4b. ensure that we haven't exceed k stops 
            if curr_stops > k:
                continue 
            
            if curr_loc in best and best[curr_loc] <= curr_stops:
                continue
            best[curr_loc] = curr_stops
            

            # 4c. determine if arrive at desination 
            if curr_loc == dst:
                min_cost = min(curr_cost, min_cost)
                continue 

            # 4e. process neighbors 
            for nei_cost, nei_loc in adjList[curr_loc]:
                heapq.heappush(min_heap, (nei_cost + curr_cost, curr_stops + 1, nei_loc))


        return min_cost if min_cost != float('inf') else -1


