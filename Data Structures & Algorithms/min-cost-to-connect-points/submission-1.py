class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        min_heap = [] 
        heapq.heappush(min_heap, (0, points[0]))

        visited = set()
        total_cost = 0

        while min_heap:

            cost, point = heapq.heappop(min_heap)
            if (point[0], point[1]) in visited:
                continue 
            
            total_cost += cost 
            visited.add((point[0], point[1]))

            for x, y in points:
                if (x,y) in visited:
                    continue 
                
                heapq.heappush(min_heap, (self.get_manhatten(point, [x,y]), [x,y]))
        
        return total_cost



    def get_manhatten(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])




        