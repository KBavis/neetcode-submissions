class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        max_heap = [] 
        res = [] 

        for i in range(len(nums)):

            # remove values from heap that are out range 
            while max_heap and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            
            # push value on and account for max 
            heapq.heappush(max_heap, (-nums[i], i))

            if i >= k - 1:
                res.append(-max_heap[0][0])
        
        return res 