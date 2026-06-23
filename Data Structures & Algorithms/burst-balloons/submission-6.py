class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
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