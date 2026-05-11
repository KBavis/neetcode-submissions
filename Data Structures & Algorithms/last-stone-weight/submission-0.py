class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # construct max heap
        heap = [] 
        for stone in stones:
            heapq.heappush(heap, -stone)
        

        # find solution 
        while len(heap) > 1:

            x = heapq.heappop(heap) # -3
            y = heapq.heappop(heap) # -2

            if x == y:
                continue 
            else:
                difference = (-1 * x) - (-1 * y)
                heapq.heappush(heap, -difference)
        
        return -1 * heap[0] if heap else 0

