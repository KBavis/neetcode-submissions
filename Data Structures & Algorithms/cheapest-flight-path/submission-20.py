class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
            Want to understand how to go through and make it to the DESTINATION from the SOURCE in the 
            CHEAPEST way possible, with the CONSTRAINT of K Stops 

            Like a Djsiktra's algorithm: whats the "cheapest" path to go from src to dst?
                --> this would work by saying once we've arrived at node, we've arrive there the cheapest way possible 
                --> instead, when we have the constraint of K stops, the "cheapest" way may lead to a scenario in which 
                    we encounter a node via our "cheapest" path, but end up not arriving there in time 
                --> dropping the set together means there's a good chance we explore paths that we've already explored and are 
                    wasteful
                --> including set means solution is broken since of our scenario 
        """

        # 1) build adj list 
        adjList = {i: [] for i in range(n)}
        for curr_src, curr_dst, curr_cost in flights:
            adjList[curr_src].append([curr_cost, curr_dst])

        print(adjList)
 
        min_heap = [(0, -1, src)]
        seen_nodes = {}


        while min_heap:


            curr_cost, curr_stops, curr_node = heapq.heappop(min_heap)
            print(f"Processing: {curr_node}, Cost={curr_cost}, Stops={curr_stops}")

            # skip if we'e seen this node before at a cheaper cost
            if curr_node in seen_nodes and seen_nodes[curr_node] <= curr_stops:
                continue


            seen_nodes[curr_node] = curr_stops

            # check if we exceed number of stops allocated
            if curr_stops > k:
                continue 
            

            # check if we found target node 
            if curr_node == dst:
                return curr_cost 
            

            # process neighbors 
            for nei_cost, nei_node in adjList[curr_node]:
                heapq.heappush(min_heap, (curr_cost + nei_cost, curr_stops + 1, nei_node))
        

        return -1 