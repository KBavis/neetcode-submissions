class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):

            if not nums:
                return 0 
            elif len(nums) <= 1:
                return nums[0]
            

            rob1 = nums[0]
            rob2 = max(nums[0], nums[1])

            # rob1, rob2, i, i + 1
            for i in range(2, len(nums)):
                temp = max(rob2, rob1 + nums[i])
                rob1 = rob2 
                rob2 = temp 
            
            return rob2 

        if not nums:
            return 0 
        elif len(nums) == 1:
            return nums[0]
        
        first = nums[1:]
        last = nums[:-1]

        return max(helper(first), helper(last))