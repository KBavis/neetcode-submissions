class KthLargest:

    def __init__(self, k: int, nums: List[int]):
       self.min_heap = [] 
       self.k = k

       for num in nums:
        self.add_to_heap(num)


    def add(self, val: int) -> int:
        return self.add_to_heap(val)
    

    def add_to_heap(self, val):
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]

        
