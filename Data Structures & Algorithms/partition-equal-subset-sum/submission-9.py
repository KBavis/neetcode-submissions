class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            Brute Force:
                - find all possible subsets (O(2^n))
                - subtract current values in the subset from total of nums 
                - if sum(curr_sub_set) == total // 2 --> return True 
        """

        self.total = sum(nums)
        return self.brute_force(nums, 0, 0)
    


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



