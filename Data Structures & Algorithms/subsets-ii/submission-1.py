class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # in each instance, we take it or leave it 
        self.res = [] 
        sorted_nums = sorted(nums)

        def dfs(idx, soFar):
            self.res.append(list(soFar)) 

            for i in range(idx, len(sorted_nums)):
                if i > idx and sorted_nums[i] == sorted_nums[i - 1]:
                    continue 
                
                soFar.append(sorted_nums[i])
                dfs(i + 1, soFar)
                soFar.pop() 

        


        dfs(0, [])
        return self.res
