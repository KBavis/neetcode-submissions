class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = [] 
        self.backtrack(nums, target, [], 0)
        return self.result

    def backtrack(self, nums, target, soFar, idx):
        if target == 0:
            self.result.append(list(soFar))
            return 
        

        for i in range(idx, len(nums)):
            if target - nums[i] >= 0:
                soFar.append(nums[i])
                self.backtrack(nums, target - nums[i], soFar, i)
                soFar.pop() 
        
