class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        self.res = 0

        def backtrack(idx, currSum):
            if idx == len(nums) and currSum == target:
                self.res += 1 
                return 
            elif idx >= len(nums):
                return 
            

            # positive first 
            backtrack(idx + 1, currSum + nums[idx])
            backtrack(idx + 1, currSum - nums[idx])
        

        backtrack(0, 0)
        return self.res 
