class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            Buy[x] --> We maximize sell on days [x + 1]
            Sell[x] --> We minimize buys on days[x + 2]

            dp[x] = max(dp[x], dp[x + 1]) - min()
        '''

        def dfs(i, holding):
            if i >= len(prices): 
                return 0 
            

            if holding:
                '''
                    We can either sell the coin today and consider buying another coin in 2 days 
                        OR 
                    We can skip selling the coin today and consider selling tomorrow 
                '''
                return max(prices[i] + dfs(i + 2, False), dfs(i + 1, True))
            else:

                '''
                    We can either buy the coin today and consider selling the coin tomorrow 
                        OR 
                    We can skip buying the coin today and consider buying tomorrow 
                '''
                return max(-prices[i] + dfs(i + 1, True), dfs(i + 1, False))
        

        return dfs(0, False)
            
            

