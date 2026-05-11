class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap =  []
        self.k = k 

        for num in nums:
            self.add_to_heap(num)
    

    def add_to_heap(self, val):
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:

        self.add_to_heap(val)

        return self.heap[0]
        
