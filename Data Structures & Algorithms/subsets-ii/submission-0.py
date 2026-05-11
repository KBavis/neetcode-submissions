class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        res = [] 
        nums.sort() 

        def dfs(soFar, idx):
            
            res.append(list(soFar))

            for i in range(idx, len(nums)):
                # this implies a sister branch is the same as previous one
                if i > idx and nums[i] == nums[i - 1] : 
                    continue
                
                soFar.append(nums[i])
                dfs(soFar, i + 1)
                soFar.pop() 

        
        dfs([], 0)

        return res 

