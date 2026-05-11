class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res = [] 

        def backtrack(soFar, idx):
            self.res.append(list(soFar))

            for i in range(idx, len(nums)):
                soFar.append(nums[i])
                backtrack(soFar, i + 1)
                soFar.pop() 


        backtrack([], 0)
        return self.res