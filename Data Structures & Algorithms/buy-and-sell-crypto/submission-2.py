class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0 
        min_buy = float('inf')

        for i in range(len(prices)):
            if min_buy > prices[i]:
                min_buy = prices[i]
            
            max_profit = max(max_profit, prices[i] - min_buy)
        
        return max_profit 
        