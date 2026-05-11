class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_buy: 
                min_buy = price 
            
            max_profit = max(max_profit, price - min_buy)
        
        return max_profit