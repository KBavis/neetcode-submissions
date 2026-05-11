class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            Accumulate sum == total_sum // 2 using nums 

            Build sum from 0 --> total_sum // 2 

            0 --> true
            1 --> true
            2 --> true
            3 --> true 
            4 --> 
        """

        # get the total sum of nums 
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False 

        # account for instances where total_sum == 0 
        if total_sum == 0 :
            return False 
        
        # target sum is half of the total sum 
        target_sum = total_sum / 2 

        memo = {}

        return self.backtrack(0, target_sum, nums, memo)


    
    def backtrack(self, idx, target_sum, nums, memo):
        if target_sum == 0:
            return True 
        elif (idx, target_sum) in memo:
            return memo[(idx, target_sum)]
        
        
        for i in range(idx, len(nums)):
            if target_sum - nums[i] >= 0:
                target_sum -= nums[i]
                
                res = self.backtrack(i + 1, target_sum, nums, memo)
                if res:
                    memo[(idx, target_sum)] = True
                    return True 
                
                target_sum += nums[i]

        memo[(idx, target_sum)] = False
        return False 
