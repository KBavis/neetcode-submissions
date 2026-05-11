class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        i = 0
        max_profit = 0
        min_buy = float('inf')


        while i < len(prices):
            
            buy = prices[i]
            if buy > min_buy:
                continue 
            
            min_buy = min(buy, min_buy)
            j = i + 1

            while j < len(prices) and prices[j] > buy:
                
                max_profit = max(max_profit, prices[j] - buy)
                j += 1
            

            i = j


        return max_profit




            
            