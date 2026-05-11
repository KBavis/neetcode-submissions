class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapping = {} 

        for i in range(len(nums)):
            if target - nums[i] in mapping:
                return [mapping[target - nums[i]], i]
            
            mapping[nums[i]] = i 
        

        return []