class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        self.res = 0

        memo = {} 

        def backtrack(idx, currSum):
            if idx == len(nums) and currSum == target:
                return 1
            elif (currSum, idx) in memo:
                return memo[(currSum, idx)]
            elif idx >= len(nums):
                return 0
            

            total_ways = 0 
            total_ways += backtrack(idx + 1, currSum + nums[idx])
            total_ways += backtrack(idx + 1, currSum - nums[idx])

            memo[(currSum, idx)] = total_ways 
            return total_ways
        

        return backtrack(0, 0)
