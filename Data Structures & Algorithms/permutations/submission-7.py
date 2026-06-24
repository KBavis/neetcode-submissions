class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        self.backtrack_non_optimal(nums, set(), [])
        return self.res 
    

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

