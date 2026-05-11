class Solution:
    def rob(self, nums: List[int]) -> int:

        seen = {}
        
        def dfs(i):
            if i >= len(nums):
                return 0 
            if i in seen:
                return seen[i]
            
            val = max(nums[i] + dfs(i + 2), dfs(i + 1))

            seen[i] = val
            return val 
        

        return dfs(0)