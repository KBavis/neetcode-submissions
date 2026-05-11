class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0

        # buy low, sell high 
        minBuy = prices[0]
        for i in range(len(prices)):
            minBuy = min(minBuy, prices[i])
            maxProfit = max(maxProfit, prices[i] - minBuy)
        

        return maxProfit