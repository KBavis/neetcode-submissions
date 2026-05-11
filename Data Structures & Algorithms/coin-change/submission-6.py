class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            amount = 12 

            fewest number of coins required to make an amount 

            1, 1, 1,1, 1,1, 1,1,1,1,1,,1 .. = 12 
            2,2,2,2,2,2,1,1,1,


            12 --> 10, 1, 1

            dp[a] --> minimum number of ways to build amount a 

            dp[a] 
                - iterate across all coins 
                - check if a - coin in dp 
                - if so, check if thats the min 

                dp[12] = ?
                    coin = 10   
                    12 - 10 ? dp[a] = dp[12-10] + 1

            need way to say impossible! float('inf')
        """

        # dp[0] = 0, dp[1] = 1

        # dp[0] = 0, dp[1] = float('inf'), dp[2] = float('inf'), dp[3] 

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 

        for a in range(amount + 1): 
            for c in coins:
                
                # check if we can build this solution
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        

        return dp[amount] if dp[amount] != float('inf') else -1