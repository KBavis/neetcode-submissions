class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """ 

        flights[i] = [from_i, to_i, price_i]

        src = starting airport 
        dst = destination airport
        src !+ dst 
        k max number of stops (not including src and dst as stop)

        Return cheapest price or -1 if not possible 

        """

        adjList = {i: {} for i in range(n)}
        

        for i in range(len(flights)):
            
            curr_src, curr_dst, curr_price = flights[i]

            adjList[curr_src][curr_dst] = curr_price

        memo = {} 

        def dfs(curr, total, stops):
            if curr == dst:
                return total
            elif stops > k: 
                return float('inf')
            elif (curr, stops) in memo:
                return memo[(curr, stops)]
            
            
            min_amount = float('inf')
            
            neighbor_airports = adjList[curr]
            for target_airport, target_price in neighbor_airports.items():
                min_amount = min(min_amount, dfs(target_airport, total + target_price, stops + 1))

            memo[(curr, stops)] = min_amount
            return min_amount 

        total = dfs(src, 0, 0)
        return total if total != float('inf') else -1

