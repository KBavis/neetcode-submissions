class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            Subset ==> [], [1, -1]

            a) Sum entire array 
            b) Subtract subset1 sum
            c) If that value is equal to subset1 sum, then we found our subset and return true 
        """

        return self.brute_force(nums)


    

    def brute_force(self, nums):
        """
            a) Calculate the sum of nums 
            b) backtracking problem 
                    - add, or continue 
        """

        total_sum = sum(nums)
        print(total_sum)

        def dfs(curr_sum, idx):
            if total_sum - curr_sum == curr_sum:
                print(f"Total Sum: {total_sum}, Curr Sum: {curr_sum}, Idx: {idx}")
                return True 
            

            for i in range(idx, len(nums)):

                curr_sum += nums[i]
                if dfs(curr_sum, i + 1):
                    return True 
                curr_sum -= nums[i]
            
            return False
        
        return dfs(0, 0)
            
                
