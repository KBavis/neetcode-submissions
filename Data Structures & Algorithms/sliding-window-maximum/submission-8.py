class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        a) create a max heap 
        b) only append to result in the case that i >= k 
        c) prior to appending, remove all out of range values 
                --> values idx <= (i - k)
        d) heap stores (val, k)
        """


        max_heap = []
        res = []

        for i in range(len(nums)):

            # process current value 
            heapq.heappush(max_heap, (-nums[i], i))

            # remove out of range vlaues 
            while max_heap and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            

            # only append to result if applicable
            if i >= k - 1:
                res.append(-1 * max_heap[0][0])
        

        return res