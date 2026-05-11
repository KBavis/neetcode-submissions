class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res = [] 

        candidates.sort()
        
        def backtrack(target, idx, soFar):
            if target == 0:
                self.res.append(list(soFar))
                return 
            

            for i in range(idx, len(candidates)):

                # IF we've seen this candidate previously at this depth of recursion, skip it to avoid duplicate branches
                if candidates[i] == candidates[i - 1] and i > idx:
                    continue
                

                if target - candidates[i] >= 0:
                    soFar.append(candidates[i])
                    backtrack(target - candidates[i], i + 1, soFar)
                    soFar.pop() 
            
                
        
        backtrack(target, 0, [])

        return self.res 