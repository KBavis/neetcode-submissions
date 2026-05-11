class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapping = {}
        for i in range(len(nums)):
            num = nums[i]

            if target - num in mapping:
                return [mapping[target - num], i]
            
            mapping[num] = i 
        
        return []
