class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        maxLis = 1

        # 1, 1, 2, 2, 3, 3, 4
        # 9, 1, 4, 2, 3, 3, 7

        dp = [1] * (len(nums) + 1)
        

        for i in range(1, len(nums), 1):
            print(nums[i])
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxLis = max(dp[i], maxLis)
        

        return maxLis 
                