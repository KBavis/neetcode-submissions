class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        """
            1) we want UNIQUE solutions even though we have duplicates 
            2) how can we ensure when we have situatiosn such as 
                    2, 2 that we don't "process" 2 twice in a speerate sister branch 

            3) skip 
        """

        res = []

        # sort candidates 
        candidates.sort() # increasing order 


        def backtrack(soFar, idx, target):
            if target == 0:
                res.append(list(soFar))
                return 
            

            for i in range(idx, len(candidates)):

                # skip re-processing elements 
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue 
                

                if target - candidates[i] >= 0:
                    soFar.append(candidates[i])
                    backtrack(soFar, i + 1, target - candidates[i])
                    soFar.pop() 

        backtrack([], 0, target)

        return res                 
                