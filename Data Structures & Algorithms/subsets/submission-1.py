class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [] 

        def search(soFar, idx):

            res.append(list(soFar))

            for i in range(idx, len(nums)):
                soFar.append(nums[i])
                search(soFar, i + 1)
                soFar.pop()


        search([], 0)
        return res