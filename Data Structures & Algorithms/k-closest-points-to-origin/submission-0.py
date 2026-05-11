class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        """
            1. Iterate through each point
            2. Calculate euclidean distance 
            3. Push on the (-1 * distance, point) onto heap
            4. If len(heap) > k --> pop off max distance to
        """

        heap = [] 
        for point in points:
            distance = self.getDistanceFromOrigin(point[0], point[1])

            heapq.heappush(heap, (-1 * distance, point))
            if len(heap) > k:
                heapq.heappop(heap)
        

        return [point for _, point in heap]

    
    def getDistanceFromOrigin(self, x, y):

        return math.sqrt(((x - 0) ** 2) + ((y - 0) ** 2))