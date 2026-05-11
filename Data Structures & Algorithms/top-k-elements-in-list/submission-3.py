class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # calculate frequency 
        mapping = {}
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1
        
        # use min heap 
        min_heap = [] 
        for num, count in mapping.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap) 
        
        return [val[1] for val in min_heap]
        