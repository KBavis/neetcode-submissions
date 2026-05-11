class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = [] 
        mapping = {}
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1

        for num, freq in mapping.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        

        return [val[1] for val in heap]