class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minBuy = float('inf')
        maxProfit = 0 

        for sell in prices:
            if sell < minBuy:
                minBuy = sell 
            
            maxProfit = max(sell - minBuy, maxProfit)
        
        return maxProfit 
