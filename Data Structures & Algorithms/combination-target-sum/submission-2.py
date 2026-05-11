class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.res = []
        
        def backtrack(soFar, currTarget, idx):
            if currTarget == 0:
                self.res.append(list(soFar))
                return 
            

            for i in range(idx, len(nums)):
                num = nums[i]

                if currTarget - num >= 0:
                    soFar.append(num)
                    backtrack(soFar, currTarget - num, i)
                    soFar.pop() 
            


        backtrack([], target, 0)
        return self.res