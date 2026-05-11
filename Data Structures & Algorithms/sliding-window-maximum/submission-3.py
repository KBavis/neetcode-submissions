class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        result = []
        
        for right in range(len(nums)):

            while q and nums[q[-1]] < nums[right]:
                q.pop() 
            
            q.append(right)

            # check if maximum contains invalid index 
            if q[0] <= right - k:
                q.popleft() 
            
            if right >= k - 1:
                result.append(nums[q[0]])
        
        return result
