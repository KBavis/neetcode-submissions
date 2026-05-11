class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.res = [] 
        self.non_optimal_solution(nums, set(), [])
        return self.res
        

    def non_optimal_solution(self, nums, seen, soFar):
        if len(soFar) == len(nums):
            self.res.append(list(soFar))
            return 
        

        for num in nums:
            if num not in seen:
                seen.add(num)
                soFar.append(num)

                self.non_optimal_solution(nums, seen, soFar)

                seen.remove(num)
                soFar.pop() 
