class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        maxIs = [1] * len(nums)
        maxContig = 1

        for i in range(1, len(nums)):
            for j in range(0, i + 1):
                if nums[j] < nums[i]:
                    maxIs[i] = max(maxIs[i], maxIs[j] + 1)
                    maxContig = max(maxContig, maxIs[i])
        

        return maxContig 
            
        