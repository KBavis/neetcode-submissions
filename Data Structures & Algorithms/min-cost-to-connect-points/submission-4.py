class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
            Goal: Find the edge for each point that will be smallest cost 

            Prims vs Kruskals Algorithm 

                - prims allows for us to choose any arbitary point and determine min cost to connect next point 
                - min heap thats (manhatten_cost, x, y)

        """

        visited = set() 
        min_heap = [] 
        heapq.heappush(min_heap, (0, points[0]))
        total_cost = 0 

        while len(visited) < len(points):
            
            curr_cost, curr_point = heapq.heappop(min_heap)

            # skip previously processed verticies
            if (curr_point[0], curr_point[1]) in visited:
                continue 
            
            # process cost and point 
            visited.add((curr_point[0], curr_point[1]))
            total_cost += curr_cost
            print(f"Total Cost: {total_cost}")

            for p in points:
                if (p[0], p[1]) not in visited:
                    heapq.heappush(min_heap, (
                        self.calc_cost(curr_point, p),
                        p
                    ))
        
        return total_cost 
            




    def calc_cost(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            
