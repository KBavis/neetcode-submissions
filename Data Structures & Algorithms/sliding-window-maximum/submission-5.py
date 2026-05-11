class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # 1. Fixed window that slides (previous max may be out of current window)
        #       - each iteration ,remove all elements of range of current index
        # 2. Efficiently extracting the max rahter than needing to re-calculate max value each time 
        #       - Heap (maxHeap)
        #       - Push tuple onto heap with value and index 
        


        heap = [] 
        res = [] 

        for i, num in enumerate(nums):

            heapq.heappush(heap, (-num, i))

            if i >= k - 1:

                # remove all elements that are outside window 
                while heap and heap[0][1] < i - (k - 1):
                    heapq.heappop(heap)

                # append to res 
                if heap:
                    res.append(-1 * heap[0][0])
        

        return res 