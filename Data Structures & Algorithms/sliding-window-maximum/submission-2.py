class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = [] 
        q = deque()  # stores indices
        

        for right in range(len(nums)):

            # remove all elements currently smaller on queue 
            while q and nums[q[-1]] < nums[right]:
                q.pop() 
            

            q.append(right) # add new element 

            # check if window exceeded left most value 
            if q[0] <= right - k:
                q.popleft() 
            

            # determine if we can update solution 
            if right >= k - 1:
                output.append(nums[q[0]])
            
        return output





