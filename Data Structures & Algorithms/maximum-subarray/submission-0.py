class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxSum = float('-inf')
        currSum = 0

        for num in nums:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)
        

        return maxSum