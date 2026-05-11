class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if not nums:
            return []
        
        mapping = {}
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1
        

        # heap
        heap = []
        for num, freq in mapping.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        
        return [num[1] for num in heap]
