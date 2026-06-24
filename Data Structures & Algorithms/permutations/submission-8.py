class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        # self.backtrack_non_optimal(nums, set(), [])
        self.backtrack_optimal(0, nums)
        return self.res 
    

    def backtrack_optimal(self, start, nums):
        if start == len(nums):
            self.res.append(list(nums))
            return 
        

        for i in range(start, len(nums)):

            # swap 
            nums[start], nums[i] = nums[i], nums[start]

            # invoke 
            self.backtrack_optimal(start + 1, nums)

            # backtrack
            nums[start], nums[i] = nums[i], nums[start]


    def backtrack_non_optimal(self, nums, seen, so_far):

        if len(so_far) == len(nums):
            self.res.append(list(so_far))
            return 

        for num in nums:
            if num not in seen:
                so_far.append(num)
                seen.add(num)

                self.backtrack_non_optimal(nums, seen, so_far)

                so_far.pop() 
                seen.remove(num)

