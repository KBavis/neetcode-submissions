class Solution:
    def rob(self, nums: List[int]) -> int:
        return (
            max(self.helper(nums, True), self.helper(nums, False))
        )

    
    # [rob1, rob2, n, n + 1, ...]
    def helper(self, nums, leftToRight):
        if not nums:
            return 0 
        elif len(nums) == 1:
            return nums[0]
        
        start, end, step = (0, len(nums) - 1, 1) if leftToRight else (len(nums) - 1, 0, -1 )

        rob1, rob2 = 0, 0
        for i in range(start, end, step):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2 
            rob2 = temp 
        
        return rob2

        