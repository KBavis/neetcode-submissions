class MedianFinder:

    def __init__(self):
        self.minHeap = [] # should have ALL values > top of maxHeap
        self.maxHeap = [] # should have ALL values < top of minHeap
        

    def addNum(self, num: int) -> None:

        # default add num to maxHeap 
        heapq.heappush(self.maxHeap, -num)

        # step 1) check if balancing is needed due to differing lengths > 2 
        if len(self.maxHeap) > 1 + len(self.minHeap): 
            top_element = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, top_element)
        
        # step 2) check if balancing needed b/c top of maxHeap > top of minHeap 
        if self.minHeap and -1 * self.maxHeap[0] > self.minHeap[0]:
            top_element = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, top_element)
        
        # step 3) check if balancing needed b/c len(maxHeap) MUST be greater than minHeap 
        if len(self.minHeap) > len(self.maxHeap): 
            top_element = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -top_element)
        
        

    def findMedian(self) -> float:
        
        total_len = len(self.minHeap) + len(self.maxHeap)

        return (-self.maxHeap[0] + self.minHeap[0]) / 2 if total_len % 2 == 0 else -self.maxHeap[0]

        
        