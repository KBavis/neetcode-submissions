class MedianFinder:

    def __init__(self):

        # two heaps, large (min heap) & small (max heap)
        # the heaps must be equal in size 
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num) # heapq is minheap by default, -1 makes it a max heap

        # ensure every element in small is <= large 
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]):

            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        

        # unven size (by 2 or greater) ? 
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        
        if len(self.large) > len(self.small):
            return self.large[0]
        

        return (-1 * self.small[0] + self.large[0]) / 2
        