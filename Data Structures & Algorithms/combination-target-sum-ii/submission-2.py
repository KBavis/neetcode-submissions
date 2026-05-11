class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res = []
        candidates.sort() 


        def comboSum(target, idx, soFar):
            if target == 0:
                self.res.append(list(soFar))
                return 
            

            for i in range(idx, len(candidates), 1):
                # skip duplicates in same level of recursion 
                if i > idx and candidates[i - 1] == candidates[i]:
                    continue
                elif target - candidates[i] >= 0:
                    soFar.append(candidates[i])
                    comboSum(target - candidates[i], i + 1, soFar)
                    soFar.pop() 
        

        comboSum(target, 0, [])
        return self.res 