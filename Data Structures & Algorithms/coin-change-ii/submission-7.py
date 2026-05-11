class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.memo = {}

        def dfs(amount, idx):
            if amount == 0:
                return 1
            elif (amount, idx) in self.memo:
                return self.memo[(amount, idx)]
            
            total_ways = 0

            for i, coin in enumerate(coins):
                if i >= idx and amount - coin >= 0:
                    total_ways += dfs(amount - coin, i)
            
            self.memo[(amount, idx)] = total_ways
            return total_ways


        return dfs(amount, 0)