class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [] 

        # max heap 
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        

        # iterate while maxHeap length > 1 
        while len(maxHeap) > 1:

            # pop two largest 
            largest = -1 * heapq.heappop(maxHeap) 
            second = -1 * heapq.heappop(maxHeap)

            if largest != second:
                heapq.heappush(maxHeap, -1 * (largest - second))


        
        return -1 * maxHeap[0] if maxHeap else 0