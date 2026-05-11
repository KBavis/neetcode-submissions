class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            Buy[x] --> We maximize sell on days [x + 1]
            Sell[x] --> We minimize buys on days[x + 2]

            dp[x] = max(dp[x], dp[x + 1]) - min()
        '''

        memo = {}

        def dfs(i, holding):
            if i >= len(prices): 
                return 0 
            

            if holding:
                '''
                    We can either sell the coin today and consider buying another coin in 2 days 
                        OR 
                    We can skip selling the coin today and consider selling tomorrow 
                '''
                max_sell = max(prices[i] + dfs(i + 2, False), dfs(i + 1, True))
                memo[i] = max_sell
                return max_sell
            else:

                '''
                    We can either buy the coin today and consider selling the coin tomorrow 
                        OR 
                    We can skip buying the coin today and consider buying tomorrow 
                '''
                max_buy = max(-prices[i] + dfs(i + 1, True), dfs(i + 1, False))
                memo[i] = max_buy
                return max_buy
        

        return dfs(0, False)
            
            

