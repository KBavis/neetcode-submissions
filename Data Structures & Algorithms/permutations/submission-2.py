class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(soFar, seen):
            if len(soFar) == len(nums):
                res.append(list(soFar))
                return 
            

            for num in nums:
                if num not in seen:
                    soFar.append(num)
                    seen.add(num)

                    backtrack(soFar, seen)

                    soFar.pop() 
                    seen.remove(num)

        backtrack([], set())
        return res