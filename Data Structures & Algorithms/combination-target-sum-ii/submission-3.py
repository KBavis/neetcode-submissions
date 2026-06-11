class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            - iterate through candidates 
            - determine if we can "utilize" the current candidate
                    --> target - candidates[i] >= 0 
            - if we can, add to "soFar" and recurse 
            - need to account for sister trees 

            O(nlogn) for the sorting 

            i > index and candidates[i] == candidates[i - 1] 

            1 1 2 --> 3 

            [[1, 2], [1,2]]

        """

        self.res = [] 

        # sort candidates in ascending order 
        candidates.sort() 

        def combo(index: int, so_far: list, curr_target: int):
            if curr_target == 0:
                self.res.append(list(so_far)) # O(n)
                return 
            

            for i in range(index, len(candidates)):
                
                # determine if we need to skip 
                if i > index and candidates[i] == candidates[i - 1]:
                    continue 
                
                # determine if we can utilize this candidate in our solution 
                if curr_target - candidates[i] >= 0:
                    curr_target -= candidates[i]
                    so_far.append(candidates[i])

                    combo(i + 1, so_far, curr_target)

                    curr_target += candidates[i]
                    so_far.pop()
            

        

        combo(0, [], target)
        return self.res

