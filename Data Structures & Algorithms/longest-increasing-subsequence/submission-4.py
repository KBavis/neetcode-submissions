class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLis = 1 
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            curr_val = nums[i]

            for j in range(i, len(nums), 1):
                if curr_val < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxLis = max(maxLis, dp[i])
        

        return maxLis 
