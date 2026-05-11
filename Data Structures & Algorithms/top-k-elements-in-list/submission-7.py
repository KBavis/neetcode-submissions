class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        mapping = {} 
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1
        


        minHeap = []
        for key, value in mapping.items():
            
            heapq.heappush(minHeap, (value, key))

            if len(minHeap) > k:
                heapq.heappop(minHeap) 
        

        return [val[1] for val in minHeap]

        