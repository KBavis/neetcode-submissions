class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        elif len(nums) == 1:
            return nums[0]

        rob1 = nums[0]
        rob2 = max(rob1, nums[1])

        for i in range(2, len(nums)):
            amount = nums[i]
            curr = max(rob1 + amount, rob2)
            rob1 = rob2
            rob2 = curr
        
        return rob2
        