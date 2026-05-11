class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res = [] 

        def dfs(so_far, idx):
            self.res.append(list(so_far)) 

            for i in range(idx, len(nums)):
                so_far.append(nums[i])
                dfs(so_far, i + 1)
                so_far.pop() 
        

        dfs([], 0)
        return self.res