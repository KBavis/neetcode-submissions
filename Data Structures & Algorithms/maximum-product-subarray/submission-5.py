class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = 1 
        currMax = 1
        res = nums[0]

        for num in nums:
            temp = currMax 
            currMax = max(num, currMax * num, currMin * num)
            currMin = min(num, temp * num, currMin * num)
            res = max(currMax, res)

        return res
        