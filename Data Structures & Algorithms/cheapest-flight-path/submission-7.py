class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Adjacency list 
            - directed graph 
            - includes price as well 

        1: {
            2: 100, 
            3: 300
        }
        """


        adjList = {i: {} for i in range(n)}
        for source, destination, price in flights: 
            adjList[source][destination] = price
        

        q = deque([(0, src)])

        curr_k = -1
        min_cost = float('inf')

        print(f"AdjList: {adjList}")
        visited = {}

        while q: 

            # ensure that we're staying under maximum stops 
            if curr_k > k:
                break

            length = len(q)
            print(f"Q: {q}, CurrK: {curr_k}")

            for i in range(length):

                curr_cost, curr_stop = q.popleft()
                if curr_stop in visited and visited[curr_stop] <= curr_cost:
                    # skip destinations seen before that were reached with cheaper costs 
                    continue 

                # this path is over since we have reached destination 
                if curr_stop == dst:
                    min_cost = min(min_cost, curr_cost)
                    continue 

                # append potential destinations to src  
                potential_destinations = adjList.get(curr_stop, {})
                if not potential_destinations:
                    continue 

                for next_dst, next_cost in potential_destinations.items():
                    q.append((curr_cost + next_cost, next_dst))
                

                
                visited[curr_stop] = curr_cost
            

            curr_k += 1 
        

        return min_cost if min_cost != float('inf') else -1
        