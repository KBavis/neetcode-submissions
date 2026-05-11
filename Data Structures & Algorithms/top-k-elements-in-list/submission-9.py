class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mapping = {}
        min_heap = [] 

        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1

        for num in mapping.keys():
            heapq.heappush(min_heap, (mapping[num], num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        

        return [val[1] for val in min_heap]
            