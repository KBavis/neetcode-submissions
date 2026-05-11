class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0 

        buy, sell = 0, 1
        max_profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell
            
            sell += 1
        
        return max_profit 


        