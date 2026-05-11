class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        heap = []   
        output = [] 

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            # only append to output once window is appropiate size
            if i >= k - 1:

                # remove max values that are out of range 
                while heap and heap[0][1] < i - (k - 1):
                    heapq.heappop(heap)
                
                output.append(-heap[0][0])
        

        return output 
