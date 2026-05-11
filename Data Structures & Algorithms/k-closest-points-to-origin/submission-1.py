class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        # construct a heap with (distance, point)
        minHeap = [] 
        for point in points:
            heapq.heappush(minHeap, (self.calculate_distance_from_origin(point), point))

        # pop of k cloest points 
        res = [] 
        for i in range(k):
            val = heapq.heappop(minHeap)
            res.append(val[1])

        return res 

    def calculate_distance_from_origin(self, point):

        return math.sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)
