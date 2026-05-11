class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = [] 
        q = deque()  # stores indices
        
        for r in range(len(nums)):
            # Remove indices whose corresponding values are smaller than current
            while q and nums[q[-1]] < nums[r]:
                q.pop() 
            
            q.append(r)
            
            # Remove indices that are outside the current window
            if q[0] <= r - k:
                q.popleft() 
            
            # Add to output when we have a complete window
            if r >= k - 1:
                output.append(nums[q[0]])  # q[0] has the index of max element
        
        return output



