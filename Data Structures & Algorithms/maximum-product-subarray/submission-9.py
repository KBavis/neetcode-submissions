class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxProd = nums[0]
        currMin = nums[0]
        currMax = nums[0]

        for num in nums[1:]:

            temp = currMax 
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(currMin * num, temp * num, num)

            maxProd = max(currMax, currMin, maxProd)
        

        return maxProd 