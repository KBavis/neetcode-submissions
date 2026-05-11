class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            1) can re-use the same number 
            2) must add to target
            3) only explore a path if its a possibility that its a solution (i.e target - nums[i] >= 0)
        """

        res = []
        
        def backtrack(soFar, idx, target):
            if target == 0:
                res.append(list(soFar))
                return 
            

            for i in range(idx, len(nums)):
                
                if target - nums[i] >= 0:
                    soFar.append(nums[i])
                    backtrack(soFar, i, target - nums[i])
                    soFar.pop() 
            
        
        backtrack([], 0, target)

        return res