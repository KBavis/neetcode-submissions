class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        leftProd = 1    
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = leftProd
            leftProd *= nums[i]
        

        rightProd = 1 
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= rightProd 
            rightProd *= nums[i]
        

        return res