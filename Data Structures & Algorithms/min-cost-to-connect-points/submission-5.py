class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
            Cost Function: |xi - xj| + |yi - yj| 

            Where to connect point (0,0) to?
                BRUTE_FORCE:
                    --> cost((0,0), (2,4))
                    --> cost((0,0), (4,2))
                    --> ...

                    Check the current point against the available set of REMAINING options 
                
                BFS / Queue 
                    --> minimum spanning tree 
                        --> find EDGES to connect each VERTEX in cheapest way possible 
                    
                    
                    --> select a arbitary point (0,0)
                    --> compute the distances on set of remaining points 
                    --> EACH POINT, will need to be accounted for 

                
                1) start at point 0,0
                2) accrue the initial cost (which is zero)
                3) compute the manhatten of "remaining" points and add this to our minHeap 
                4) pop off min heap, skip points that have been visited
        """

        if not points or len(points) == 1:
            return 0 
        
        visited = set() 

        # min_heap = (cost, point_x, point_y)
        min_heap = [(0, points[0][0], points[0][1])]
        total_cost = 0

        while min_heap:
            
            # step 1. grab cheapest cost off of min heap to connect next edge 
            cost, point_x, point_y = heapq.heappop(min_heap)

            # step 2. ensure this point hasn't been accounted for
            if (point_x, point_y) in visited:
                continue  
            
            # step 3. mark as visited and acrue cost 
            visited.add((point_x, point_y))
            total_cost += cost 

            # step 4. chekc if we've visited all nodes 
            if len(visited) == len(points):
                return total_cost 

            # step 5. compute cost for next node to draw edge to 
            for nei_x, nei_y in points:
                if (nei_x, nei_y) not in visited:
                    heapq.heappush(min_heap, (self.calc_cost(nei_x, nei_y, point_x, point_y), nei_x, nei_y))
        

        return total_cost 

    
    def calc_cost(self, nei_x, nei_y, og_x, og_y):
        return abs(nei_x - og_x) + abs(nei_y - og_y)


