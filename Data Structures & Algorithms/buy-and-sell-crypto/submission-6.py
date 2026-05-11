class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        minBuy = prices[0]
        maxProfit = 0 


        for sell in prices:
            if sell < minBuy:
                minBuy = sell 
            
            maxProfit = max(sell - minBuy, maxProfit)
        
        return maxProfit 