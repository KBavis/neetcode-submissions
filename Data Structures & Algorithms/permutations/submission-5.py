class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.res = [] 
        # self.non_optimal_solution(nums, set(), [])
        self.optimal_solution(0, nums)
        return self.res
        


    def optimal_solution(self, start, nums):
        if start == len(nums):
            self.res.append(nums[:])
            return 
        

        for idx in range(start, len(nums)):

            # swap start and current element 
            nums[start], nums[idx] = nums[idx], nums[start]

            self.optimal_solution(start + 1, nums)

            # swap back
            nums[start], nums[idx] = nums[idx], nums[start]


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
