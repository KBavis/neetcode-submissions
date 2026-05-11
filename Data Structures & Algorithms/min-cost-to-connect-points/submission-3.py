class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        min_heap = [] 
        heapq.heappush(min_heap, (0, points[0]))
        total_cost = 0

        visited = set() 
        while min_heap:

            cost, curr_point = heapq.heappop(min_heap)
            x, y = curr_point[0], curr_point[1]

            if (x, y) in visited:
                continue 
            
            total_cost += cost 
            visited.add((x, y))

            for point in points:
                curr_x, curr_y = point[0], point[1]

                if (curr_x, curr_y) in visited:
                    continue 
                
                heapq.heappush(min_heap, (self.manhatten(x, curr_x, y, curr_y), point))
        

        return total_cost
        

    
    def manhatten(self, x1, x2, y1, y2):
        return abs(x1 - x2) + abs(y1 - y2)