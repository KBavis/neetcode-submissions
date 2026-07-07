class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            Brute Force:
                - find all possible subsets (O(2^n))
                - subtract current values in the subset from total of nums 
                - if sum(curr_sub_set) == total // 2 --> return True 
        """
        memo = {}
        target_sum = sum(nums) / 2
        if not target_sum.is_integer():
            return False 

        def optimized(curr_sum, idx):
            if (curr_sum, idx) in memo:
                return memo[(curr_sum, idx)]
            elif target_sum == curr_sum:
                return True
            elif idx >= len(nums):
                return False 

            success = False 
            for i in range(idx, len(nums)):
                curr_sum += nums[i]
                
                value = optimized(curr_sum, i + 1)
                if value == True:
                    success = True 
                    break 
                
                curr_sum -= nums[i]

            memo[(curr_sum, idx)] = success
            return success
        

        return optimized(0, 0)


        


    def brute_force(self, nums, idx, curr_sum):
        if curr_sum == self.total / 2:
            return True 
        elif idx >= len(nums):
            return False
        

        for i in range(idx, len(nums)):
            curr_sum += nums[i]
            if self.brute_force(nums, i + 1, curr_sum):
                return True 
            curr_sum -= nums[i]
        

        return False



