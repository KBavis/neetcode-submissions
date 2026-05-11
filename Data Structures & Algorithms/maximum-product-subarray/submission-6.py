class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxProd = nums[0]
        currMin = 1 
        currMax = 1

        for num in nums:
            temp = currMax
            currMax = max(num, temp * num, currMin * num)
            currMin = min(num, temp * num, currMin * num)
            maxProd = max(maxProd, currMax)
        

        return maxProd 