class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)
        leftProd = 1

        for i in range(len(nums)):
            result[i] = leftProd 
            leftProd *= nums[i]


        rightProd = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= rightProd 
            rightProd *= nums[j]
        
        return result
