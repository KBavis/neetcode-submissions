class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxSub = nums[0]
        currSum = nums[0]

        for num in nums[1:]:
            currSum = max(currSum + num, num)
            maxSub = max(maxSub, currSum)
        
        return maxSub 