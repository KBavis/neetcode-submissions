class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            Decision Tree:
                Can we take the current number and still be <= target? If so, take it, and recurse 
                If not, continue to next value 

                Backtrackign type problem
        """

        self.res = []

        def combo(idx, target, soFar):
            if target == 0:
                self.res.append(list(soFar))
            
            for i in range(idx, len(nums), 1):
                if target - nums[i] >= 0:
                    soFar.append(nums[i])
                    combo(i, target -nums[i], soFar)
                    soFar.pop() 
        

        combo(0, target, [])

        return self.res 