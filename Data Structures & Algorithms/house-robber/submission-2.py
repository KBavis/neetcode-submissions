class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        if len(nums) == 1:
            return nums[0]
        

        mapping = {0: nums[0], 1: max(nums[0], nums[1])}
        for i in range(2, len(nums)):
            mapping[i] = max(nums[i] + mapping[i - 2], mapping[i - 1])
        
        return mapping[len(nums) - 1]
        