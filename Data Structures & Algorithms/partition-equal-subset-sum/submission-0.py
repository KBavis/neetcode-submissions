class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        """
            Does a partition require elemenets? 

            Given a list of integers 

            Find subsets where the two arrays are equal to eachother  

            Backtracking 
                partition1 = list 
                partition1_sum = integer 

                look for situation where partition1_sum == target sum 
                    - this implies that we can partition it 


            15 --> 7.5 
                --> if total sum % 2 != 0 --> return False 


            if target_sum == 0:
                return True 

            for i in range
            
            if target_sum - nums[i] >= 0:
                target_sum - nums[i]
                backtrack 
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

        return self.backtrack(0, target_sum, nums)


    
    def backtrack(self, idx, target_sum, nums):
        if target_sum == 0:
            return True 
        
        
        for i in range(idx, len(nums)):
            if target_sum - nums[i] >= 0:
                target_sum -= nums[i]
                if self.backtrack(i + 1, target_sum, nums):
                    return True 
                target_sum += nums[i]


        return False 