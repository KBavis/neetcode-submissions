class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        res = [] 

        def backtrack(seen, soFar):
            if len(soFar) == len(nums):
                res.append(list(soFar))
                return 
            

            for num in nums:
                if num not in seen: # if we haven't seen this number in the current recursive branch 
                    seen.add(num)
                    soFar.append(num)

                    backtrack(seen, soFar)

                    seen.remove(num)
                    soFar.pop() 

            
        
        backtrack(set(), [])

        return res

