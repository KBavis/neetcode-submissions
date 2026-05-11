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

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False 

        target_sum = total_sum // 2


        dp = [False] * (target_sum + 1)
        dp[0] = True

        for num in nums:

            for curr_sum in range(target_sum, num - 1, -1):
                if curr_sum - num >= 0:
                    dp[curr_sum] |= dp[curr_sum - num]
        

        return dp[target_sum]
