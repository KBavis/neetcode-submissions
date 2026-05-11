class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = []
        self.k = k

        for num in nums:
            self.add_to_heap(num)


    def add_to_heap(self, val):

        heapq.heappush(self.maxHeap, val)
        if len(self.maxHeap) > self.k:
            heapq.heappop(self.maxHeap)

    def add(self, val: int) -> int:
        
        self.add_to_heap(val)

        return self.maxHeap[0]
        
