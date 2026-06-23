class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # return self.brute_force(nums)
        return self.efficient_solution(nums)


    def brute_force(self, nums):
        
        max_coins = 0
        for i in range(0, len(nums)):

            # calculate total coins for popping currnet ballon
            left_coin = nums[i - 1] if i - 1 >= 0 else 1
            right_coin = nums[i + 1] if i + 1 < len(nums) else 1 
            total_coins = left_coin * nums[i] * right_coin 

            # calculate remaining coins after removing current ballong 
            remaining_ballons = nums[:i] + nums[i + 1:] if i + 1 < len(nums) else nums[:i] + []
            remaining_coins = self.brute_force(remaining_ballons)

            max_coins = max(remaining_coins + total_coins, max_coins)
        
        return max_coins 
    
    def efficient_solution(self, nums):
        
        memo = {}

        def dfs(l, r):
            if l > r:
                return 0 
            elif (l,r) in memo:
                return memo[(l,r)]
            
            max_coins = 0
            for i in range(l, r + 1):

                # recurse down each path know that we're popping the ith ballon last 
                left_coin = nums[l - 1] if l - 1 >= 0 else 1 
                right_coin = nums[r + 1] if r + 1 < len(nums) else 1
                curr_coins = left_coin * nums[i] * right_coin

                max_coins = max(
                    max_coins,
                    dfs(l, i - 1) + curr_coins + dfs(i + 1, r)
                )
            
            memo[(l,r)] = max_coins
            return max_coins 


        left = 0 
        right = len(nums) - 1 
        return dfs(left, right)